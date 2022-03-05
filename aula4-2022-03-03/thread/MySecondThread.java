package thread;

import counter.ICounter;

public class MySecondThread extends Thread {
	private ICounter myCounter;
	private int ID;

	public MySecondThread(int ID, ICounter myCounter) {
		this.ID = ID;
		this.myCounter = myCounter;
	}

	@Override
	public void run() {
		myCounter.increment();
	}

	public ICounter getMyCounter() {
		return myCounter;
	}

	public int getID() {
		return ID;
	}

}
