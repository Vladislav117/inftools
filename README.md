# inftools
Repository with useful fuctions for EGE
# How to use?
Run `python inftools.py -a <action>` to call action.
<table>
  <tr><td colspan="3" align="center"><b>Actions</b></td></tr>
  <tr><td>init</td><td>Generates files and directories.</td><td>init, prep, initialize, prepare, install</td></tr>
  <tr><td>pattern</td><td><i>In process...</i></td><td></td></tr>
  <tr><td>clear</td><td>Clears all generated files and backups. Remove ".inftools" file before calling.</td><td>clear, unistall</td></tr>
  <tr><td>calc</td><td>Shows results in previous and secondary forms.</td><td>calc, result, results, check, answers</td></tr>
  <tr><td>pack</td><td>Packs all files (including user files) to archive.</td><td>pack, zip, arch, archive</td></tr>
  <tr><td>backup</td><td>Packs all files (including user files) to archive and saves to /backups folder.</td><td>backup</td></tr>
</table>

# Initializing
Run `python inftools.py -a init` to initialize inftools. It wil generate for you next files:
* answers.txt - Here you can write your answers. If answer is correct, change `[]` to `[v]` or to `[+]`.
* notes.txt - Here you can write some text.
* solutions - In this folder you can find empty python files for your solutions.
* backups - There will be backups of the project.
* .inftools - Special file. It protects you from removing data with commands.

# Answers
Run `python inftools.py -a calc` to show results.
You should change `answers.txt` file select which answer is right. Just replace `[]` to `[v]` or `[+]`.

# Archiving
Run `python inftools.py -a pack` to archive all files (except backups and other archives).
It will create .zip file.

# Backups
Run `python inftools.py -a backup` to backup all files (except other backups and archives).
It will create .zip file in the `/backups` folder.
BE CAREFUL: `clear` function removing all backups, but not archives.

# Uninstalling
Run `python inftools.py -a clear` to remove all automatically generated file (including backups, exculding archvies).
