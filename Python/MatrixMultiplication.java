package com.company;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Scanner;
public class Matrix {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int r1 = 3;
        int c1 = 2;
        int r2 = 2;
        int c2 = 3;
        int [][] a1 = {{1, 2}, {3, 4}, {5, 6}};
        int [][] a2 = {{1, 2, 3}, {4, 5, 6}};
        ArrayList<ArrayList<Integer>> a = new ArrayList<>();
        for (int i = 0; i < r1; i++) {
            a.add(new ArrayList<>());
        }
        for (int i = 0; i < r1; i++)
        {
            for (int j = 0; j < c2; j++) {
                int s = 0;
                for (int k = 0; k < r2; k++) {
                    s += a1[i][k]*a2[k][j];
                }
                a.get(i).add(s);
            }
        }
        System.out.println(a);

    }
}
