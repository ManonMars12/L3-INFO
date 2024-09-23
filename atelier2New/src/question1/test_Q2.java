package question1;

import java.time.LocalDate;

import question1.Employe; 
import question1.Secretaire;
import question1.Manager;

public class test_Q2 {

	public static void main(String[] args) {
		
		
		
		LocalDate date1 = LocalDate.of(1990, 5, 15);
		LocalDate date2 = LocalDate.of(2020, 5, 15);

		Employe e1 = Employe.createEmploye("Marie", "Jeanne", date1, 1200.0, date2);
		System.out.println(e1.getSalaire()); 
		e1.augmenterSalaire(10); 
		System.out.println(e1.getSalaire()); 
		
		Secretaire s2 = Secretaire.createSecretaire("Julie", "Jeanne", date1, 1200.0, date2);
		
		Manager m1 = Manager.createManager("Marie", "Jeanne", date1, 1200.0, date2, s2);
		System.out.println(m1.getSalaire()); 
		m1.augmenterSalaire(10); 
		System.out.println(m1.getSalaire()); 
		
		
		Secretaire s1 = Secretaire.createSecretaire("Marie", "Jeanne", date1, 1200.0, date2);
		System.out.println(s1.getSalaire()); 
		s1.ajouterManager(m1);
		s1.augmenterSalaire(10); 
		System.out.println(s1.getSalaire()); 
		
		
		}

}
