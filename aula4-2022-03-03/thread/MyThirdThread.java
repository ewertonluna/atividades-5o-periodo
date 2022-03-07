package thread;

import counter.ICounter;

public class MyThirdThread extends Thread {
	private ICounter myCounter;
	private int ID;

	public MyThirdThread(int ID, ICounter myCounter) {
		this.ID = ID;
		this.myCounter = myCounter;
	}

	@Override
	public void run() {
		myCounter.increment();
		System.out.println("ID da thread: " + ID); // Solução da letra E
	}
	
	public int getID() {
		return ID;
	}
	
}
