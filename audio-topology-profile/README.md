# Audio topology

## To test

To check the drop-in:
```
$ systemctl --user cat pipewire
```

To check the real affinity:
```
$ taskset -cp $(pgrep pipewire)
```

To check the pipewire threads:
```
$ ps -eLo pid,tid,psr,cls,rtprio,comm | grep pipewire
```

To check real time priorities:
```
$ chrt -p $(pgrep -x pipewire)
```

To check the configuration:
```
$ systemctl --user show pipewire | grep CPUAffinity
```

To activate the service:
```
$ systemctl --user enable audio-topology.service
$ systemctl --user start audio-topology.service
```

## Example

### Before

```
$ systemctl --user cat pipewire
# /usr/lib/systemd/user/pipewire.service
[Unit]
Description=PipeWire Multimedia Service

# We require pipewire.socket to be active before starting the daemon, because
# while it is possible to use the service without the socket, it is not clear
# why it would be desirable.
#
# A user installing pipewire and doing `systemctl --user start pipewire`
# will not get the socket started, which might be confusing and problematic if
# the server is to be restarted later on, as the client autospawn feature
# might kick in. Also, a start of the socket unit will fail, adding to the
# confusion.
#
# After=pipewire.socket is not needed, as it is already implicit in the
# socket-service relationship, see systemd.socket(5).
Requires=pipewire.socket dbus.service 
ConditionUser=!root

[Service]
LockPersonality=yes
MemoryDenyWriteExecute=yes
NoNewPrivileges=yes
SystemCallArchitectures=native
SystemCallFilter=@system-service mincore
Type=simple
ExecStart=/usr/bin/pipewire
Restart=on-failure
Slice=session.slice

[Install]
Also=pipewire.socket
WantedBy=default.target

# /usr/lib/systemd/user/pipewire.service.d/00-uresourced.conf
[Service]
Slice=session.slice

# /usr/lib/systemd/user/service.d/10-timeout-abort.conf
# This file is part of the systemd package.
# See https://fedoraproject.org/wiki/Changes/Shorter_Shutdown_Timer.
#
# To facilitate debugging when a service fails to stop cleanly,
# TimeoutStopFailureMode=abort is set to "crash" services that fail to stop in
# the time allotted. This will cause the service to be terminated with SIGABRT
# and a coredump to be generated.
#
# To undo this configuration change, create a mask file:
#   sudo mkdir -p /etc/systemd/user/service.d
#   sudo ln -sv /dev/null /etc/systemd/user/service.d/10-timeout-abort.conf

[Service]
TimeoutStopFailureMode=abort
```

```
$ taskset -cp $(pgrep -x pipewire)
pid 1636's current affinity list: 0-7
```

### After

```
$ systemctl --user cat pipewire
# /usr/lib/systemd/user/pipewire.service
[Unit]
Description=PipeWire Multimedia Service

# We require pipewire.socket to be active before starting the daemon, because
# while it is possible to use the service without the socket, it is not clear
# why it would be desirable.
# /usr/lib/systemd/user/pipewire.service
[Unit]
Description=PipeWire Multimedia Service

# We require pipewire.socket to be active before starting the daemon, because
# while it is possible to use the service without the socket, it is not clear
# why it would be desirable.
#
# A user installing pipewire and doing `systemctl --user start pipewire`
# will not get the socket started, which might be confusing and problematic if
# the server is to be restarted later on, as the client autospawn feature
# might kick in. Also, a start of the socket unit will fail, adding to the
# confusion.
#
# After=pipewire.socket is not needed, as it is already implicit in the
# socket-service relationship, see systemd.socket(5).
Requires=pipewire.socket dbus.service 
ConditionUser=!root

[Service]
LockPersonality=yes
MemoryDenyWriteExecute=yes
NoNewPrivileges=yes
SystemCallArchitectures=native
SystemCallFilter=@system-service mincore
Type=simple
ExecStart=/usr/bin/pipewire
Restart=on-failure
Slice=session.slice

[Install]
Also=pipewire.socket
WantedBy=default.target

# /usr/lib/systemd/user/pipewire.service.d/00-uresourced.conf
[Service]
Slice=session.slice

# /usr/lib/systemd/user/pipewire.service.d/10-audio-topology.conf
[Service]
CPUAffinity=2 3 4 5 6 7

# /usr/lib/systemd/user/service.d/10-timeout-abort.conf
# This file is part of the systemd package.
# See https://fedoraproject.org/wiki/Changes/Shorter_Shutdown_Timer.
#
# To facilitate debugging when a service fails to stop cleanly,
# TimeoutStopFailureMode=abort is set to "crash" services that fail to stop in
# the time allotted. This will cause the service to be terminated with SIGABRT
# and a coredump to be generated.
```

```
$ taskset -cp $(pgrep pipewire)
pid 1648's current affinity list: 0-7
taskset: failed to set pid 1648's affinity: Argument invalide
```
