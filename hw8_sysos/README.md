# UNIX tools written with Python


## Functions


- **wc.py** - analogous to UNIX **wc** function with -l, -w and -c options

Usage example: 
```commandline
wc.py -l -w -c
wc.py -l -w -c file
```
- **ls.py** - analogous to UNIX **ls** function

Usage example: 
```commandline
ls.py
ls.py path/to/dir/
```

- **sort.py**  - analogous to UNIX **sort** function, but with no flags 

Usage example: 
```commandline
sort.py textfile
```
- **rm.py** - analogous to UNIX **rm** function. Has -r flag.

Usage example: 
```commandline
rm.py file
rm.py -r directory
```
## Usage

To execute the commands from your directory without 'python' command, place the scripts into your directory and 
make them executable by `chmod +x <script_name.py>`.

After that, the scripts will be executable directly like that:

`./script_name.py`
