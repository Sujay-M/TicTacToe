classdef TicTacToe
    %TICTACTOE Summary of this class goes here
    %   Detailed explanation goes here
    
    properties(GetAccess = 'public', SetAccess = 'private')
        players;
        board;
        turn;
    end
    
    methods
        function obj = TicTacToe(pname1,pname2)
            obj.players = [];
            if nargin==0
                obj.players = [obj.players struct('board',zeros(3,3),'pname','Jarvis','ptype',0)];
                obj.players = [obj.players struct('board',zeros(3,3),'pname','Tars','ptype',0)];
            elseif nargin==1
                obj.players = [obj.players struct('board',zeros(3,3),'pname',pname1,'ptype',1)];
                obj.players = [obj.players struct('board',zeros(3,3),'pname','Tars','ptype',0)];
            elseif nargin==2
                obj.players = [obj.players struct('board',zeros(3,3),'pname',pname1,'ptype',1)];
                obj.players = [obj.players struct('board',zeros(3,3),'pname',pname2,'ptype',1)];
            end
            obj.board = zeros(3,3);
            obj.turn = 1;
        end
        function status = winCheck(obj)
            if sum(any(sum(obj.players(obj.turn).board,1)==3))~=0 || sum(any(sum(obj.players(obj.turn).board,2)==3))~=0
                status = 1;
            elseif trace(obj.players(obj.turn).board)==3 || trace(fliplr(obj.players(obj.turn).board))==3
                status = 1;
            else
                status = 0;
            end
        end
        function  [obj,status] = makeMove(obj,r,c)
            if obj.board(r,c)==1
                status = -1;
            else
                obj.players(obj.turn).board(r,c) = 1;
                status = obj.winCheck();
            end
        end
        function [] = display(obj)
            clc;
            for i=1:3
                for j=1:3
                    if obj.players(1).board(i,j)==1
                        fprintf('X ');
                    elseif obj.players(2).board(i,j)==1
                        fprintf('O ');
                    else
                        fprintf('- ');
                    end
                end
                fprintf('\n');
            end
        end
        function [obj] = start(obj)
            fprintf('game starts\n');
            status=0;
            rng('shuffle');
            while status==0 && sum(sum(obj.board))~=9
                obj.display();
                if obj.players(obj.turn).ptype==1
                    status = -1;
                    while status==-1
                        coor = input('enter coordinate 1-9\n');
                        [c,r] = ind2sub([3,3],coor);
                        [obj,status] = obj.makeMove(r,c);
                    end
                else
                    status = -1;
                    while status==-1
                        coor = randi(9);
                        [c,r] = ind2sub([3,3],coor);
                        [obj,status] = obj.makeMove(r,c);
                    end
                end
                obj.turn = mod(obj.turn,2)+1;
                obj.board(r,c)=1;
                
            end
            obj.display();
            if status==0
                fprintf('game draw\n');
            else
                fprintf('%s is the winner\n',obj.players(mod(obj.turn,2)+1).pname);
            end
        end
    end
    
end

