import re


def parse_log(log_text):
    result = {}
    section_regex = re.compile("=====.*?=====")
    sections = section_regex.split(log_text)
    # Timestamp
    result["time_stamp"] = sections[0].strip()
    # Disk usage
    disk_sec = sections[1].split()
    result["disk_1kblocks"] = disk_sec[8]
    result["disk_used"] = disk_sec[9]
    result["disk_available"] = disk_sec[10]
    result["disk_usePercent"] = disk_sec[11]
    # Memory
    mem_sec = [elem.strip().split() for elem in sections[2].split("\n")]
    result["mem_total"] = mem_sec[1][0]
    result["mem_used"] = mem_sec[2][0]
    result["mem_active"] = mem_sec[3][0]
    result["mem_inactive"] = mem_sec[4][0]
    result["mem_free"] = mem_sec[5][0]
    result["mem_buffer"] = mem_sec[6][0]
    result["mem_swap"] = mem_sec[7][0]
    # Uptime
    result["up_date"] = sections[3].strip()
    # Processes
    proc_sec = sections[5].strip().split('\n')
    for program_line in proc_sec:
        program_split = program_line.split()
        program_name = program_split[0]
        result["{}_pid".format(program_name)] = program_split[1:]
    # Docker version
    try:
        result["docker_version"] = sections[6].strip().split()[2].replace(",", "")
    except IndexError:
        result["docker_version"] = None
    # Docker IDs
    docker_sec = sections[7].strip().split('\n')
    result["docker_ids"] = docker_sec
    # OS info
    os_sec = [line.split('\t') for line in sections[9].strip().split('\n')]
    result["os_distributor"] = os_sec[0][1]
    result["os_description"] = os_sec[1][1]
    result["os_release"] = os_sec[2][1]
    result["os_codename"] = os_sec[3][1]
    # Hostname
    result["hostname_hostname"] = sections[10].strip()
    return result
