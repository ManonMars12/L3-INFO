package q1;

import java.time.LocalDate;

public class Manager extends Employe {
	
	
	private Secretaire secretaire; 
	
	public Manager(String nom,int age, String prenom, LocalDate date, double salaire, LocalDate date_embauche, Secretaire secretaire) {
		super (nom, age, prenom, date, salaire, date_embauche);
 
		this.secretaire=secretaire;
	}

	
	
	public static Manager createManager(String nom,int age, String prenom, LocalDate date, double salaire, LocalDate date_embauche, Secretaire secretaire){
		if ((age<16) || (age>65)) {
			return(null);
		}
		else {
			Manager e = new Manager(nom, age, prenom, date, salaire, date_embauche, secretaire);
			return(e);
		}
}
	
	



	public Secretaire getSecretaire() {
		return secretaire;
	}



	public void setSecretaire(Secretaire secretaire) {
		this.secretaire = secretaire;
	}

	

	public void augmenterSalaire(int pourcentage) {
		if (pourcentage<0) {
			return; 
		}
		else {
		this.setSalaire(this.getSalaire()+(this.getSalaire()*((pourcentage + (0.5*calculAnnuite()))* Math.pow(10, -2)))); /* Math.pow c'est la puissance */ 
		}
		
	}

}