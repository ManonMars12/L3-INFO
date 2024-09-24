package q1;

import java.util.ArrayList;
import java.util.Random;

import q1.Case;
import q1.Joueur;

public class Jeu {
	
	private String titre;
	private static final int NB_JOUEUR_MAX = 6; 
	private static final int NB_CASES = 50; 
	private ArrayList<Joueur> joueurs; 
	private Case[] cases; 
	private int nbEtapes; 
	private int nbObstacles; 
	private  static int scoreMax; 
	
	public Jeu(String titre, int nbEtapes, int nbObstacles) {
		this.titre=titre;
		this.nbEtapes=nbEtapes;
		this.nbObstacles=nbObstacles;
		this.scoreMax=-10000; 
		joueurs = new ArrayList<>(); 
		cases =  new Case[NB_CASES]; 
		
	}
	
	public void ajouterJoueur(Joueur j) {
		joueurs.add(j);
	}
	
	public ArrayList tousLesPerso() {
		ArrayList<Personnage> res = new ArrayList<>(); 
		for (int i=0; i < joueurs.size(); i++) {
			Joueur joueur_courant = joueurs.get(i);
			ArrayList<Personnage> listePerso = joueur_courant.getListe_perso();
			
			for (int j=0; j < listePerso.size(); j++) {
				res.add(listePerso.get(j));
				
			}
			
		}
		return(res);
	}
	

	public void initialiserCases() {
        Random rand = new Random();
        int obstaclesAjoutes = 0;

        for (int i = 0; i < NB_CASES; i++) {
            int montantGains = rand.nextInt(NB_CASES) + 1; 
            cases[i] = new Case(montantGains);


            if (montantGains % 5 == 0 && obstaclesAjoutes < nbObstacles) {
                int penalite = montantGains * 2; 
                Obstacle obstacle = new Obstacle();
                obstacle.setPenalite(penalite);
                cases[i].setObs(obstacle); 
                obstaclesAjoutes++;
            }
        }

	}
	public void lancerJeu() {
		initialiserCases(); 
		for (Joueur joueur : joueurs) {
			 ArrayList<Personnage> liste_personnage = joueur.getListe_perso();
		        for (Personnage personnage : liste_personnage) {
		            for (int j = 0; j < NB_CASES; j++) {
		                if (cases[j].estLibre()) {
		                    cases[j].placerPersonnage(personnage);
		                    personnage.setPosition(j);
		                    break; 
		                }
		            }
		        }
			}
		ArrayList<Personnage> liste_personnage = tousLesPerso(); 
		for (int i=0; i<nbEtapes; i++) {
			for (Personnage personnage : liste_personnage) {
				int posSouhaitee=personnage.positionSouhaitee();
				personnage.setPosition(posSouhaitee);
				Joueur proprietaire = personnage.getProprietaire();
				if (cases[posSouhaitee].estLibre()) {
					personnage.deplacer(posSouhaitee, cases[posSouhaitee].getGain());
				}
				
				if ((cases[posSouhaitee].getObs() != null ) || (cases[posSouhaitee].getPerso() != null )) {
					proprietaire.modifierPoints(-1 * (cases[posSouhaitee].getGain()));
				}
				
				if (posSouhaitee > NB_CASES) {
					personnage.deplacer(50, cases[posSouhaitee].getGain());
				}
			
			}
			
		}
		afficherParticipants();
		afficherCases();
		afficherResultats();
		
	}

	
	public void afficherParticipants() {
		System.out.println("LISTE DES JOUEURS");
		System.out.println("-----------------");
		for (int i=0; i<joueurs.size(); i++) {
			System.out.println(joueurs.get(i).toString()); 
		}
	}
	
	public void afficherCases() {
		System.out.println("----------------------"); 

		System.out.println("Liste des cases : "); 
		for (int i=0; i<NB_CASES; i++) {
			System.out.println(cases[i].toString()); 
		}
	}
	
	public void afficherResultats() {
		Joueur gagnant = null;
        int score_max = scoreMax; 
        for (Joueur joueur : joueurs) {
            if (gagnant == null || joueur.getNb_points() > gagnant.getNb_points()) {
                gagnant = joueur;
            }
        }
        

		System.out.println(titre);
		System.out.println("***************************************");
		System.out.println("RESULTATS "); 
		System.out.println("Le gagant est " + gagnant.getNom() + " avec " + gagnant.getNb_points() + " points ");

        if (gagnant != null && gagnant.getNb_points() > scoreMax) {
        	int ancien_scoreMax=scoreMax; 
            scoreMax = gagnant.getNb_points();
        }
 
	}

	public int getScoreMax() {
	    return scoreMax;
	}
	
}
