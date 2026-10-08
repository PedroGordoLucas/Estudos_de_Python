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
