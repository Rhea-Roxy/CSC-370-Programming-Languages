package com.company;

import java.util.Scanner;

public class RunLengthEncode2 {

    public static String Code(String string) {
        String new_string = "";
        string+= " ";
        int count = 0;
        int i = 0;
        int j = 0;
        while (j <= string.length() - 1) {
            if (string.charAt(i) == string.charAt(j)) {
                count += 1;
                j += 1;

            } else {
                if (count > 4)
                    new_string += "/0" + String.valueOf(count) + string.charAt(i);
                else {
                    for (int k = 0; k < count; k++)
                        new_string += string.charAt(i);
                }
                count = 0;
                i = j;
            }

        }

        return new_string;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string to be encoded: ");
        System.out.println(Code(sc.nextLine()));

    }


}
