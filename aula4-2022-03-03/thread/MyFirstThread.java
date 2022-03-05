package thread;

import counter.ICounter;

public class MyFirstThread extends Thread {
	private ICounter myCounter;
	private int ID;

	public MyFirstThread(int ID, ICounter myCounter) {
		this.ID = ID;
		this.myCounter = myCounter;
	}

	@Override
	public void run() {
		for (int i = 0; i < 1000; i++) {
			myCounter.increment();
		}
	}

	public int getID() {
		return ID;
	}

	public ICounter getMyCounter() {
		return myCounter;
	}
	
}
