![Hydrogen](Hydrogen.wiki/img/logo.png)

## About
Hydrogen is a simple programming language like python, containing similar syntax, logic, and functions.
However, if you're not careful with the language... Then, like hydrogen, it'll blow up in your face.
The language is meant to be easy to learn and understand in order to ease you into learning other new languages. And when you're done with it, you can remove it.

Hydrogen is also a good programming language for making games or software due to it's efficiency. Hydrogen already comes with some starter projects, including introductory code for teaching users how to both use Hydrogen and analyze it's syntax to build upon the skill of being able read code as if it were just regular english. Included in these starter projects are some example games and software that make use of multiple different methods in order to run.

## How to Use
### Install:
To install hydrogen, download the installer on the release page and run as administrator.
<br>
![Installer](Hydrogen.wiki/img/installer.png)
<br>
Then press `Next`, this should take you to the modules page, where you can choose which modules you want to install (You can always come back and install other ones later).

### Uninstall:


## Syntax
The syntax for Hydrogen is sort of a mix between [Python](https://www.python.org/) and [Javascript](https://developer.mozilla.org/en-US/docs/Web/javascript)
where declaring variables is like javascript but function declaration keywords are more like python.

#### Variables:
```
let my_variable: str = "Hello World!";

const my_constant: int = 6 + 5 * 2;
```
#### Loops:
```
while (`condition`) {
    ...
}

for (`condition`) {
    ...
}
```
#### Functions:
```
def myFunction(*args, **kwargs) {
    ...
}

myFunction();
```
#### Objects:
```
class MyObject(SuperClass) {
    ...
}

my_object = MyObject()
```
#### Subclasses:
```
class MasterClass {
    def mySubclass(self, *args, **kwargs) {
        ...
    }
}

my_master_class = MasterClass();

my_master_class.mySubclass();
```