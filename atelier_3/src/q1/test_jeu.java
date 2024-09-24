package q1;

public class test_jeu {

	public static void main(String[] args) {
		
		Jeu jeu = new Jeu("Atelier POO", 4, 10); 
		Tauren t1 = new Tauren("Hector", 15, 10); 
		Humain h1 = new Humain("Jean", 10); 
		
		Tauren t2 = new Tauren("Hercule", 20, 5); 
		Humain h2 = new Humain("Marie", 10); 
		
		Joueur j1 = new Joueur("Paul"); 
		Joueur j2 = new Joueur("Lucien"); 
		
		j1.ajouterPersonnage(t1);
		j1.ajouterPersonnage(h1);
		
		j2.ajouterPersonnage(t2);
		j2.ajouterPersonnage(h2);
		
		jeu.ajouterJoueur(j1);
		jeu.ajouterJoueur(j2);
	
		jeu.lancerJeu();
		jeu.lancerJeu();
		jeu.lancerJeu();
		jeu.lancerJeu();
		jeu.lancerJeu();
		
		System.out.println("Reccord battu : nouveau score max : " + jeu.getScoreMax() + " points "); 
		

	}
	
}


