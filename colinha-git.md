GIT:

{STATUS}: Serve pra verificar como ta a situação do repositório atual,
ver se um arquivo foi adicionado ou removido.

{ADD}: prepara o arquivo que vai para um proximo commit,
tem que lembrar que o comando é " git add 'nome do arquivo' ".

{COMMIT -m}: Esse comando serve pra fechar o conteúdo e deixar um recado
pra quem for querer saber o que é, o comando sendo " git commit -m 'msg' ".

{PUSH}: Manda os arquivos para o github(o origin), o comando
sendo "git push".

{SWITCH}: Esse ai troca entre qualquer branch já existente, se usar o
sufixo "-c", assim "git switch -c <nome>", ele cria e entra na branch, mas
caso queira só trocar, basta usar só "git switch <nome existente>".

{MERGE}: Junta/Mescla o que foi feito no rascunho(branch) na main, se nada
foi feito na main enquanto isso, o merge so vai avancar(fast-forward), mas
caso alguem mexeu, ele ainda funciona e cria um commit pra avisar, vai dar
BO se alguem mexeu na mesma linha do mesmo arquivo.

{BRANCH -d}: Usando o comando branch mais o sufixo "-d", deleta a branch com
segurança, o comando sendo "git branch -d <nome da branch>", se usar o -D o
bagulho é deletado a força.

{GITIGNORE}: Arquivo que serve como "porteiro": lista o que o Git deve
ignorar (cache, senhas, venv), para não aparecer no git status nem subir
com o git add. Só vale para arquivos ainda não rastreados; se já foi
commitado, usa "git rm --cached nome".

{DIFF}: mostra linha por linha o que mudou. "git diff" = o que editei e
ainda não dei add. "git diff --staged" = o que já dei add e ainda não
commitei. Linhas com - foram removidas, com + foram adicionadas.

{RESTORE}: desfaz coisas. "git restore --staged arq" tira da caixa (desfaz o
add, mantém a edição). "git restore arq" descarta a edição e volta ao último
commit (não tem volta, confere com git diff antes).
