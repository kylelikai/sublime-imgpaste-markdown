# Imgpaste - Markdown - Subl Plugin

Allow a user to copy paste a Screenshot in Sublime-Text when using Markdown
The output will be in markdown form to automate the process for Sublime-Text user

When the keybinds is pressed, you must specify the name of the saved image (from clipboard)

Every screenshots will be saved in the directory 'screenshots' in the current directory of the opened file
If the directory doesn't exist, it will create it

**Linux Only**

This plugin was inspired by https://github.com/berendkleinhaneveld/sublime-image-paste 

```bash
## Output - For Example
# after press ctrl+alt+v

![](./screenshots/my_image.png)
```

![](https://github.com/Naerz/sublime-imgpaste-markdown/blob/main/demo.gif)

## Prerequisites

`xclip` needs to be installed:

```sh
apt-get install xclip
```

## Installation

```bash
cd <USER_CONFIG>/sublime-text-3/Packages/
git clone https://github.com/Naerz/sublime-imgpaste-markdown.git

# Or

git clone https://github.com/Naerz/sublime-imgpaste-markdown.git <USER_CONFIG>/sublime-text-3/Packages/sublime-imgpaste-markdown/
```

**Example**

```bash
cd /home/kali/.conf/sublime-text-3/Packages/
git clone https://github.com/Naerz/sublime-imgpaste-markdown.git

# OR

git clone https://github.com/Naerz/sublime-imgpaste-markdown.git /home/kali/.conf/sublime-text-3/Packages/sublime-imgpaste-markdown/
```

## Usage

Use the command: 'image-paste: Paste image'
(Default key-binding set to CMD+ALT+V) to paste the image.

*Refer to keymap file*

## Settings

Use the `folder` setting to configure where to store the image.
`${folder}` will be substituted with the currently opened folder.
`${file_path}` will be substituted with the folder that contains
the currently opened file (default setting).

**This version was tested only using `${file_path}`**
