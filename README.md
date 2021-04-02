# Plover Run Shell

Command plugin for [Plover](https://github.com/openstenoproject/plover) to run an arbitrary shell
command.

The package is available on [GitHub](https://github.com/user202729/plover_run_shell) and
[PyPI](https://pypi.org/project/plover-run-shell/).

## Usage

In order to use this plugin in [Plover](https://github.com/openstenoproject/plover) you need to
create a dictionary entry of the form:

``` json
{
    "example_stroke": "{PLOVER:SHELL:command}"
}
```

Note:

* The command might be executed synchronously (so you can use `&` on Linux or `start` on Windows if
  you don't want Plover to freeze, in case the called process is long-running).
* (on UNIX systems) The command may be executed by the `sh` shell.  If you want to use another
  shell, you can call that shell explicitly: `bash -c "command"`.

## Example

These examples are only for X on GNU/Linux systems (it relies on many external tools).

You should be able to construct similar translations by searching for "how to do task X from
console/command-line".

If there's none, you can still write an external program with other programming language and call it
from Plover. (alternatively, write it in Python and make a command plugin)

Alternatively, if you already have a working binding in the windows manager, you don't have to use
this plugin and use Plover's key combination syntax.

* Shutting down the machine

		"{PLOVER:SHELL:\\{ sleep 2s;poweroff; \\}&}{PLOVER:QUIT}"

* Restart Plover (console GUI, in a new terminal)

		"{PLOVER:SHELL:xterm -e bash -c \"sleep 0.5s; plover --gui console\" &}{PLOVER:QUIT}"

* Change brightness

		"{PLOVER:SHELL:xbacklight -10}"
		"{PLOVER:SHELL:xbacklight +10}"

* Change volume (note that the solution with `pactl` is not robust because it relies on the sink
  number being 0)

		"{PLOVER:SHELL:pactl set-sink-volume 0 -5%}"
		"{PLOVER:SHELL:pactl set-sink-volume 0 +5%}"
		"{PLOVER:SHELL:amixer -D pulse sset Master 5%+}"
		"{PLOVER:SHELL:amixer -D pulse sset Master 5%-}"

* Suspend (depends on your GNU/Linux distribution)

		"{PLOVER:SHELL:systemctl suspend}"
		"{PLOVER:SHELL:pm-suspend}"
