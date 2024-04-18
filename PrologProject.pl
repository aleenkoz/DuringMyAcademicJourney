/* Time of Day */

saudiTime(X):-
    get_time(T),
    stamp_date_time(T,date(_,_,_,H,_,_,_,_,_),'UTC'),
    X is H+3.
greeting:-
    saudiTime(X),(X>=0, X<12 ->  write('Good morning, user!'),nl);
    saudiTime(X),(X>=12, X<17 ->  write('Good afternoon, user!'),nl);
    saudiTime(X),(X>=17, X<21 ->  write('Good evening, user!'),nl).
/*This function displays the (Welcome message)*/
welcome :-
    write('Welcome to the Game Recommendation System!'),nl,
    write('Choose your preferred genres and consoles.'),nl,
    write('Please write your answers in small letters.'),nl.

/*The followig code is a simple Knowledge Base of games*/
game('The Past Within', co_operative, pc).
game('It takes two', co_operative, playstation).
game('Valorant', action_adventure, pc).
game('Ghost of Tsushima', action_adventure, playstation).
game('Little Nightmares 2', puzzle, pc).
game('The Talos Principal', puzzle, playstation).
game('Forza Horizon', sports, pc).
game('Kartrider: Drift', sports, playstation).
game('Call of Duty', survival, pc).
game('Grounded', survival, playstation).

/*The following code initializes dynamic data structure for recommendations*/
:- dynamic recommended_games/1.

/*The following code validates inputs*/
valid_genre(Genre) :-
    member(Genre, [co_operative, action_adventure, puzzle, sports, survival]).

valid_console(Console) :-
    member(Console, [pc, playstation]).

/*The following function asks for user preferences*/
ask_preferences(Genre, Console) :-
    writeln('Choose your preferred genre: co_operative, action_adventure, puzzle, sports, survival'),
    read(Genre),
    valid_genre(Genre),
    writeln('Choose your preferred Console: pc, playstation'),
    read(Console),
    valid_console(Console).

/*The following code recommends games based on the chosen preferences*/
recommend_games(Genre, Console) :-
    findall(Game, game(Game, Genre, Console), Matches),
    retractall(recommended_games(_)), /*Clear previous recommendations*/
    asserta(recommended_games(Matches)).

/*The following code picks a random game from the recommended games*/
pick_game(Game) :-
    recommended_games(Games),
    random_member(Game, Games), /*Selects a random game*/
    show_game_details(Game).

/*The following function shows game details*/
show_game_details(Game) :-
    game(Game, Genre, Console),
    format('You will enjoy:\nGame: ~w\nGenre: ~w\nConsole: ~w\n', [Game, Genre, Console]),
    write('Have Fun!').

/*The following code represents the main loop*/
start :-
    welcome,
    repeat,
    ask_preferences(Genre, Console),
    recommend_games(Genre, Console),
    (recommended_games([]) ->
        write('You have entered false information'),nl,
        fail; /*Fails the repeat loop to return to asking preferences*/
        pick_game(_),
        ! /*This cut prevents the program from backtracking further than this point*/
    ).

/*This code was developed by: Aleen Alzahrani- Rihaaf Bugis- Fatimah Alghamdi- Lina Bashmakh- Nour Abou Elnour*/

