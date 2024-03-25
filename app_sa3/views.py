from django.shortcuts import render

# Create your views here.

contexto = {
    'jogos': [
       #tpTexto = 1 -> Título
       #tpTextp = 2 -> Jogo
        {'nome': 'Inicio', 'tpTexto' : 1, 'url': '', 'tpFocus' : 1},
        {'nome': 'Rocket League', 'tpTexto' : 2, 'imagem': '/static/img/jogo_rocket_league.jpg',
         'tpFocus' : 0, 'site' : 'https://www.rocketleague.com/pt-br' , 'texto1': 'Rocket League é um jogo eletrizante que combina elementos de futebol e corrida em uma experiência única. Os jogadores controlam carros potentes equipados com foguetes, competindo em arenas dinâmicas enquanto tentam marcar gols em seus oponentes. Com física realista e uma jogabilidade frenética, Rocket League oferece uma experiência multiplayer viciante, onde a estratégia e a habilidade se combinam em partidas emocionantes.', 
          'texto2' : 'Prepare-se para acelerar, driblar e voar pelos campos de jogo, enquanto compete em torneios emocionantes e desafia seus amigos em intensas disputas. Acesse agora o site oficial do jogo e junte-se à comunidade de milhões de jogadores que tornaram Rocket League um fenômeno global.', 'url' : 'rocket-league','review' : 'Bem-vindo ao jogo estilo arcade de futebol e caos automobilístico! Personalize seu carro, entre em campo e compita em um dos jogos de esportes mais aclamados de todos os tempos!'},
        {'nome': 'Minecraft', 'tpTexto' : 2, 'imagem': '/static/img/jogo_minecraft.jpg', 'tpFocus' : 0, 'review' : 'O Minecraft é um jogo formado por blocos, criaturas e uma comunidade. Os blocos podem ser usados para transformar o mundo ou construir criações fantásticas. Não há maneira errada de jogar, a não ser que você cave direto para baixo.'
         , 'url' : 'minecraft', 'site' : 'https://www.minecraft.net/pt-br/about-minecraft', 'texto1' : 'Minecraft é um universo de possibilidades infinitas, onde a criatividade e a sobrevivência se encontram em um mundo feito de blocos. Desde o seu lançamento em 2009, tornou-se um fenômeno global, atraindo jogadores de todas as idades para construir, explorar e enfrentar aventuras em paisagens geradas proceduralmente. Com modos de jogo que vão desde o pacífico Criativo ao desafiador Sobrevivência, Minecraft oferece uma experiência personalizável que permite aos jogadores redefinir o mundo ao seu redor'
         , 'texto2' : 'A beleza de Minecraft reside na sua simplicidade gráfica e na profundidade de seu gameplay. Blocos podem ser quebrados, criados e colocados para remodelar a paisagem ou construir criações fantásticas. Criaturas podem ser combatidas ou amigas, dependendo do seu estilo de jogo. Seja embarcando em aventuras épicas sozinho ou com amigos, não há maneira errada de jogar.'}
       , {'nome': 'Fortnite', 'tpTexto' : 2, 'imagem': '/static/img/jogo_fortnite.jpg', 'url' : 'fortnite',
         'tpFocus' : 0, 'site' : 'https://www.fortnite.com/?lang=pt-BR' , 'review' : 'Fortnite é um jogo multijogador online de estilo Battle Royale, onde até 100 jogadores competem para ser o último sobrevivente em uma ilha que encolhe progressivamente.',
         'texto1': 'Fortnite é um fenômeno global no mundo dos jogos eletrônicos, desenvolvido pela Epic Games e lançado em 2017. É um jogo de sobrevivência de mundo aberto, onde até 100 jogadores lutam em uma batalha para ser o último sobrevivente. Os jogadores podem coletar recursos, construir estruturas e procurar armas para aumentar suas chances de sobrevivência. Com um estilo vibrante e cartunesco, Fortnite se destaca por sua jogabilidade acessível e eventos ao vivo que mantêm o jogo sempre atualizado e interessante.', 
          'texto2' : 'Existem três modos principais de jogo em Fortnite: “Salve o Mundo”, onde os jogadores cooperam para sobreviver contra hordas de zumbis; o “Modo Criativo”, que permite aos jogadores construir mundos e desafios personalizados; e o mais popular, “Battle Royale”, onde os jogadores competem sozinhos ou em equipes para serem os últimos sobreviventes em uma ilha que diminui de tamanho devido a uma tempestade que se fecha. Este último modo ajudou a popularizar o gênero Battle Royale e contribuiu significativamente para o sucesso estrondoso do jogo.'}
         ,{'nome': 'Sobre', 'tpTexto' : 1, 'url': 'sobre', 'tpFocus' : 0}
         
        
        ]
   
    }

def tela_inicio(request):
   for jogo in contexto['jogos']:
       if jogo['nome'] == 'Inicio':
            jogo['tpFocus'] = 1
       else:
            jogo['tpFocus'] = 0
   return render(request, 'app_sa3/inicio.html', contexto) 

def rocket_league(request): 
   for jogo in contexto['jogos']:
         if jogo['nome'] == 'Rocket League':
             jogo['tela_principal'] = 1
             jogo['tpFocus'] = 1
         else:
            jogo['tela_principal'] = 2
            jogo['tpFocus'] = 0
   return render(request, 'app_sa3/jogo_principal.html', contexto) 

def minecraft(request): 
   for jogo in contexto['jogos']:
      if jogo['nome'] == 'Minecraft':
         jogo['tela_principal'] = 1
         jogo['tpFocus'] = 1
      else:
         jogo['tela_principal'] = 2
         jogo['tpFocus'] = 0
   return render(request, 'app_sa3/jogo_principal.html', contexto) 

def fortnite(request): 
   for jogo in contexto['jogos']:
      if jogo['nome'] == 'Fortnite':
         jogo['tela_principal'] = 1
         jogo['tpFocus'] = 1
      else:
         jogo['tela_principal'] = 2
         jogo['tpFocus'] = 0
   return render(request, 'app_sa3/jogo_principal.html', contexto) 

def sobre(request):
   for jogo in contexto['jogos']:
      if jogo['nome'] == 'Sobre':
         jogo['tpFocus'] = 1
      else:
         jogo['tpFocus'] = 0
   return render(request, 'app_sa3/sobre.html', contexto)
   

