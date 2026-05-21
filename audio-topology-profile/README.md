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
