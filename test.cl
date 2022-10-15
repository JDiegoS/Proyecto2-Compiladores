class Main {
   a : Int;
   d : Int;
   c : Int;
    b : Bool <- false;

    main() : SELF_TYPE {
        {

            if not (a < b) then c <- (c + b) else c <- (d + b) fi;
        }
    } ;


};