import os
from platform import system
from socket import socket as sock
import socket
from time import sleep

MITM_PORT = 8888


def get_pid_by_port(port):
    if "windows" == system().lower():
        find_port = 'netstat -aon|findstr "%s" ' % port
        print("windows暂不适配")
        return
    else:
        find_port = "lsof -i:%s" % port
    result = os.popen(find_port).read()
    if not result:
        print('port %s is not use' % port)
        return []
    lines = [_ for _ in result.split(os.linesep) if _]
    title = lines.pop(0)
    pids = [int(line.split(' ')[2]) for line in lines]
    return pids


def kill_port_process(pids):
    import signal
    for pid in pids:
        os.kill(pid, signal.SIGKILL)
    if pids:
        print('shutdown mitmweb')


def shutdown(port=MITM_PORT):
    # kill process which use port
    return kill_port_process(get_pid_by_port(port))


def help_message():
    msg = "launch: launch mitmweb -p 8888 -s {addon} addon defalut is repaly_requests_addon.py\n" \
          "shutdown: shutdown mitmweb process.\n" \
          "quit: shutdown mitmweb process and exit."
    print(msg)


def get_addon_py(want: str):
    try:
        addon_py = want.split(' ')[1] or "repaly_requests_addon.py"
    except IndexError as e:
        addon_py = "repaly_requests_addon.py"
    except Exception as e:
        print(type(e), e)
        addon_py = "repaly_requests_addon.py"
    if not os.path.exists(addon_py):
        print('addon file %s not found' % addon_py)
        return ''
    return addon_py


def launch(want: str):
    addon_py = get_addon_py(want)
    addon = {}
    if addon_py:
        addon = {"addon": ' -s %s ' % addon_py}
    else:
        print('without add launch mitmweb')
        addon = {"addon": ''}
    addon['port'] = 8888
    s = sock(socket.AF_INET, socket.SOCK_STREAM)
    if 0 == s.connect_ex(('127.0.0.1', MITM_PORT)):
        quit()
    cmd = 'nohup mitmweb -p {port} {addon} &'.format_map(addon)
    # print(cmd)
    os.system(cmd)
    sleep(1)


def main():
    title = ['[l]aunch', '[s]hutdown', '[q]uit', '[h]elp']
    title_str = '\t'.join(title)
    os.system('clear')
    print(title_str)
    while True:
        want = input(">")
        os.system('clear')
        print(title_str)
        if not want:
            continue
        if 'l' == want[0]:
            launch(want)
        elif 's' == want[0]:
            shutdown()
        elif 'q' == want[0]:
            shutdown()
            break
        elif 'clear' == want:
            os.system('clear')
            print(title_str)
        else:
            help_message()


if __name__ == "__main__":
    main()
