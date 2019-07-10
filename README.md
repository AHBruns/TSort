# TSort

### Description

TSort also known as Moen or Moenize (named after my algs. and data 
structures professor, James Moen) is a command-line utility that topologically 
sorts paragraphs based on their conceptual dependency. This sorting process is 
known as topological sorting, hence the formal name, TSort.

### Installation

For simplicity here's the oneliner. Run the following in your terminal:

`git clone https://github.com/AHBruns/TSort.git && chmod +x TSort/install.sh && ./TSort/install.sh`

Once run, you'll likely have to restart your terminal. After this the utility
 can be called on any file by running any of the following commands:
 
 - `tsort relative/path/to/input/file relative/path/to/output/file`
 - `moen relative/path/to/input/file relative/path/to/output/file`
 - `moenize relative/path/to/input/file relative/path/to/output/file`
 
 **NOTE: The output can overwrite existing files. So, be sure to write to 
 either a non-existent file or an existing file that you're okay with 
 overwriting.**
 

### Usage

TSort uses a simple domain-specific language to mark-up paragraphs. The 
TSort language is made up of statements. Each statement gets its own line; no 
sharing. Additionally, statements are tethered to their proceeding paragraph. 
That is, you should write your document like so:
```
PARAGRAPH A's STATMENTS

PARAGRAPH A

PARAGRAPH B's STATEMENTS

PARAGRAPH B

``` 
All TSort statements take the form `||| OPERATION ENTITY`.
 
The pipes are there to tell the parser that the line being parsed is a TSort statement, 
not a content line. So, ensure that you don't accidentally proceed any of 
your content lines with three pipes.

Now let's skip ahead and look at the entity part of a statement. In the 
TSort DSL entities are simply names for concepts being discussed in the 
content of the text.

For instance, if you had a paper about binary trees you 
might have an entity for the concept of a node, a linked list, a binary 
search tree, an OBST, and likely many other things as well. Entities are how 
TSort reasons about which how to order your paragraphs. Importantly, entities
 can include any character except for a newline.

Finally, the operation part of the statement can be any of the following:

- `DEC` : Used to declare a new entity.
- `DESC`: Used to denote that the proceeding paragraph describes an entity.
- `DEP` : Used to denote that the proceeding paragraph depends on an entity.

Operations are actions taken on entities. For an entity to be declared the 
statement `||| DEC ENTITY` must be used. Before an entity can be described or
 depended on, it must be declared. Declaring an entity does NOT implicitly 
 cause the proceeding paragraph to describe the entity. In other words,
```
||| DEC entity1
blah blah blah
blah blah blah
blah blah blah

||| DEP entity1
blah blah blah
blah blah blah
blah blah blah
```
has no valid ordering solution, but
```
||| DEC entity1
||| DESC entity1
blah blah blah
blah blah blah
blah blah blah

||| DEP entity1
blah blah blah
blah blah blah
blah blah blah
```
does. Look in the src/test.txt for examples on how to structure your 
documents.

### Support

Please email me at alex.h.bruns@gmail.com with any questions. I can also be 
found on Twitter, @AlexHBruns.



