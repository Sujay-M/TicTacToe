clc;
clear all;
choice = input('enter the choice 1.vs cpu  2.vs player \n');
if choice==1
    pname1 = input('enter player1 name\n','s');
    Game = TicTacToe(pname1);
elseif choice==2
    pname1 = input('enter player1 name\n','s');
    pname2 = input('enter player2 name\n','s');
    Game = TicTacToe(pname1,pname2);
else
    fprintf('no input\n cpuvscpu\n'); 
    Game = TicTacToe();
end
Game = Game.start();