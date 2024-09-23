package q1;

import java.time.LocalDate;

public class Personne {
	//Attributs ou variables d'instances
	private String nom;
	private int age;
	private static int init_ID=0; 
	private int ID; 
	private String prenom; 
	private LocalDate date; 
	
	//Constructeur
	public Personne(String nom,int age) {
		this.nom=nom;
		this.age=age;
		this.ID=init_ID; 
		init_ID=init_ID+1;
		
		
	}
	
	
	public Personne(String nom,int age, String prenom, LocalDate date) {
		this.nom=nom;
		this.age=age;
		this.ID=init_ID; 
		init_ID=init_ID+1;
		this.prenom=prenom;
		this.date=date;

		
	}
	
	public Personne() {
		this("",0);
	}	
	public  void setNom(String nom) {
		this.nom=nom;
	}
	public  void setAge(int age) {
		this.age=age;
	}
	public void afficher() {
		System.out.println("Nom : "+this.nom + "\nAge : " + this.age );
	}
	public String toString() {
		return this.nom + " (" + this.age + " ans)";
	}
	
	public static int getNbPersonne() {
		return(init_ID); 
	}
	
	public static boolean plusAgee(Personne p1, Personne p2) {
		if (p1.age > p2.age) {
			return(true);
		}
		else {
			return(false);
		}
		
	}
	
	public boolean plusAgee2(Personne p1) {
		if (this.age > p1.age) {
			return(true);
		}
		else {
			return(false);
		}
		
	}
	
	public boolean equals (Personne p2){
		String nomP1 = this.getNom() ; 
		String nomP2 = p2.getNom();
		String prenomP1 = this.getPrenom();
		String prenomP2 = p2.getPrenom();
		String dateP1 = this.getDate().toString(); 
		String dateP2 = p2.getDate().toString(); 
		if ((nomP1.equals(nomP2)) && (prenomP1.equals(prenomP2)) && (dateP1.equals(dateP2))) {
			return(true);
		}
		else {
			return(false); 
			
		}
	}

	public LocalDate getDate() {
		return date;
	}

	public void setDate(LocalDate date) {
		this.date = date;
	}

	public String getNom() {
		return nom;
	}

	
	public String getPrenom() {
		return prenom;
	}
	
	public int getAge() {
		return age;
	}
}

