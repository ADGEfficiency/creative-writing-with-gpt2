# Creative Writing with GPT-2

## Data

The data is structured - the program will look for the `clean.txt` file.  

```bash
data/$AUTHOR_NAME/clean.txt
```

For completeness you can also include any code you used to create your `clean.txt` in the same folder:

```
$ ls data/asimov
clean.txt
i-robot.ipynb
raw.txt
```

I've included a few authors I like to write with:

```
$ tree -L 1 data
data
├── alan-watts
├── art-of-war
├── asimov
├── bible
├── harry
├── hemingway
├── mahabarta
├── meditations
├── plato
└── tolkien
```



## Blog post

components
- tokenizer
