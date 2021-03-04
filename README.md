# Plover Run Shell

Command plugin for [Plover](https://github.com/openstenoproject/plover) to run an arbitrary shell command.

The package is available on [GitHub](https://github.com/user202729/plover_run_shell).

## Usage

In order to use this plugin in [Plover](https://github.com/openstenoproject/plover) you need to create a dictionary entry of the form:

``` json
{
    "example_stroke": "{PLOVER:SHELL:command}"
}
```

Note:

* The command might be executed synchronously (so you can use `&` on Linux or `start` on Windows
if you don't want Plover to freeze, in case the called process is long-running).
* (on UNIX systems) The command may be executed by the `sh` shell.
If you want to use another shell, you can call that shell explicitly: `bash -c "command"`.
