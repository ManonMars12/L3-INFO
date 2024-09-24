package q1;

import q1.Personnage;
import q1.Obstacle; 

public class Case {
	
	private int gain; 
	private Personnage perso; 
	private Obstacle obs;
	
	public Case(Obstacle obs, int gain ) {
		this.obs=obs;
		this.gain=gain;
		this.perso=null;
		
	}
	
	public Case(int gain) {
		this.obs=null;
		this.perso=null;
		this.gain=gain; 
		
	}
	
	public int getPenalite() {
		if (this.obs==null) {
			return(0);
		}
		else {
			return(obs.getPenalite()); 
		}
	}
	
	public void placerPersonnage(Personnage perso) {
		this.perso=perso;
	}
	
	public void enleverPersonnage(Personnage perso) {
		this.perso=null;
	}
		
	public void placerObstacle(Obstacle obs) {
		this.obs=obs;
	}

	public boolean estLibre() {
		if ((this.obs==null) && (this.perso==null)) {
			return(true);
		}
		else {
			return(false);
		}
	}
	public boolean sansObstacle() {
		return(this.obs == null);
	}
	
	public boolean sansPersonnage() {
		return(this.perso == null);
	
	}
	
	public String toString() {
		if (estLibre()) {
			return("Libre (gain = " + this.gain + " )");
		}
		if (sansObstacle() == false) {
			return("Obstacle (pénalité = - " + this.getPenalite() + " )"); 
		}
		else {
			return (perso.toString() + (" (pénalité - " + gain + " )" ));
		}
	}

	public int getGain() {
		return gain;
	}

	public void setGain(int gain) {
		this.gain = gain;
	}

	public Personnage getPerso() {
		return perso;
	}

	public void setPerso(Personnage perso) {
		this.perso = perso;
	}

	public Obstacle getObs() {
		return obs;
	}

	public void setObs(Obstacle obs) {
		this.obs = obs;
	}

	
}

