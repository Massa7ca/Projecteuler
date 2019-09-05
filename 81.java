package javaapplication1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class JavaApplication1 {
//"c:\\81.txt"

    public static void main(String[] args) throws FileNotFoundException{

        ArrayList<ArrayList<Integer>> matricha = nachni(fail_v_matrizhu());
        
        ArrayList<ArrayList<Integer>> matricha_nov = new ArrayList<>();
        for (int i = 0; i != matricha.size(); i++){
            ArrayList<Integer> nov;
            nov = (ArrayList<Integer>) matricha.get(i).clone();
            matricha_nov.add(nov);
        }
        for(int i = 0; i != matricha_nov.size()-1; i++){
            for(int j = 1; j != matricha_nov.size(); j++){
                int per = matricha_nov.get(i).get(j);
                int vtor = matricha_nov.get(i+1).get(j-1);
                int tretiy = matricha.get(i+1).get(j);
                int menishi = min(per, vtor);
                matricha_nov.get(i+1).set(j, menishi + tretiy);
            }
            
        }
        for(int i = 0; i != matricha_nov.size(); i++){
            System.out.println(matricha_nov.get(i));
        }
        }
    

    public static Integer min(int a, int b){
        if (a < b){
            return a;
        }
        else if (a > b){
            return b;
        } 
        else{
            return a;
        }
        
    }
    
    public static ArrayList<ArrayList<Integer>> nachni(ArrayList<ArrayList<Integer>> matricha){
        int suma = 0;
        for(int i = 0; i != matricha.size(); i++){
            suma += matricha.get(0).get(i);
            matricha.get(0).set(i, suma);
        }
        suma = 0;
        for(int i = 0; i != matricha.size(); i++){
            suma += matricha.get(i).get(0);
            matricha.get(i).set(0, suma);
        }
        return matricha;
        
    }


    public static ArrayList<Integer> razdeli(String stroka) {
        ArrayList<Integer> nov = new ArrayList<>();
        String n = "";
        for (int i = 0; i != stroka.length(); i++) {
            String i_p = stroka.substring(i, i + 1);
            n += i_p;
            if (",".equals(i_p)) {
                int razmer = n.length();
                int chislo = Integer.parseInt(n.substring(0, razmer - 1));
                nov.add(chislo);
                n = "";
            }
        }
        return nov;
    }

    public static ArrayList<ArrayList<Integer>> fail_v_matrizhu() throws FileNotFoundException {
        String s = "";
        Scanner in = new Scanner(new File("c:\\81.txt"));
        ArrayList<ArrayList<Integer>> matricha = new ArrayList<>();
        while (in.hasNext()) {
            matricha.add(razdeli(in.nextLine()));
        }
        return matricha;
    }
}