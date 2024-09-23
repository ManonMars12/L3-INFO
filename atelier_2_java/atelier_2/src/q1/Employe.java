package q1;

import java.time.LocalDate;

public class Employe extends Personne{
	
	private double salaire;
	private LocalDate date_embauche; 
	
	protected Employe(String nom,int age, String prenom, LocalDate date, double salaire, LocalDate date_embauche) {
		super(nom, age, prenom, date);
		this.salaire=salaire; 
		this.date_embauche=date_embauche;
		
	}
	
	public static Employe createEmploye(String nom,int age, String prenom, LocalDate date, double salaire, LocalDate date_embauche){
		if ((age<16) || (age>65)) {
			return(null);
		}
		else {
			Employe e = new Employe(nom, age, prenom, date, salaire, date_embauche);
			return(e);
		}
		
	}
	
	public void augmenterSalaire(int pourcentage) {
		if (pourcentage<0) {
			return; 
		}
		else {
		this.salaire=salaire+(salaire*(pourcentage* Math.pow(10, -2))); /* Math.pow c'est la puissance */ 
		}
		
	}

	public double getSalaire() {
		return salaire;
	}

	public void setSalaire(double salaire) {
		this.salaire = salaire;
	}
	
	
	public LocalDate getDateEmbauche() {
		return(date_embauche); 
	}
	
	public int calculAnnuite() {
		int annee = this.getDateEmbauche().getYear();
		LocalDate date_mtn = LocalDate.now();
	    int annee_courante =  date_mtn.getYear();
		return(annee_courante-annee);
	}
		
}
	
	

	


