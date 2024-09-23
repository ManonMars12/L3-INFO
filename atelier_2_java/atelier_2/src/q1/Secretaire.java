package q1;

import java.time.LocalDate;

public class Secretaire extends Employe{
	
	private Manager[] Manager;
	private final int NBMAXMANAGER=5;
	private int nb_manager=0; 
	

	public Secretaire (String nom,int age, String prenom, LocalDate date, double salaire, LocalDate date_embauche) {
		super (nom, age, prenom, date, salaire, date_embauche);
		Manager = new Manager[NBMAXMANAGER];
		
	}

	public void ajouterManager(Manager manager) {
        if (nb_manager < NBMAXMANAGER) {
            Manager[nb_manager] = manager;
            nb_manager=nb_manager+1;
        }
        else {
        	System.out.println("Impossible trop de managers ");
        }
	}
	
	
	public void supprimerManager(Manager manager, int numero_a_supp) {
        if (nb_manager > 0) {
            Manager[numero_a_supp] = null ;
            nb_manager=nb_manager-1;
        }
        else {
        	System.out.println("Impossible pas assez de managers ");
        }
	}
	
	public Manager[] getManager() {
		return Manager;
	}

	public void setManager(Manager[] manager) {
		Manager = manager;
	}

	public int getNb_manager() {
		return nb_manager;
	}

	public void setNb_manager(int nb_manager) {
		this.nb_manager = nb_manager;
	}

	public void augmenterSalaire(int pourcentage) {
		if (pourcentage<0) {
			return; 
		}
		else {
		this.setSalaire(this.getSalaire()+(this.getSalaire()*((pourcentage + (0.1*nb_manager))* Math.pow(10, -2)))); /* Math.pow c'est la puissance */ 
		}
		
	}
	
	
	public static Secretaire createSecretaire(String nom,int age, String prenom, LocalDate date, double salaire, LocalDate date_embauche){
		if ((age<16) || (age>65)) {
			return(null);
		}
		else {
			Secretaire e = new Secretaire(nom, age, prenom, date, salaire, date_embauche);
			return(e);
		}
}
	
}
