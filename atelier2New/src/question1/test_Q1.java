package question1;

import question1.Personne; 
import java.time.LocalDate;

public class test_Q1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		LocalDate date1 = LocalDate.of(1990, 5, 15);
		LocalDate date2 = LocalDate.of(1991, 5, 15);
		LocalDate date3 = LocalDate.of(1992, 5, 15);
		 
		
		Personne p1 = new Personne("Marie", "Jeanne", date1); 
		Personne p2 = new Personne("Jean", "Je", date2);
		Personne p3 = new Personne("Marie", "Jeanne", date1); 
		System.out.println(Personne.getNbPersonne()); /*Attendu 3 */
		System.out.println(p1.equals(p2)); /*Attendu False*/
		System.out.println(p1.equals(p3)); /*Attendu True */
		System.out.println(Personne.plusAgee(p1,p2)); /*Attendu True */
		System.out.println(Personne.plusAgee(p2,p1)); /*Attendu False*/
		System.out.println(p1.plusAgee2(p2)); /*Attendu True */
		System.out.println(p2.plusAgee2(p1)); /*Attendu False*/
		
	}

}
