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
		long start = System.nanoTime();
		for (int i = 0; i < 1000; i++) {
			myCounter.increment();
		}
		long end = System.nanoTime();
	System.out.println("Runtime da execução de run() da Thread é de " + (end - start) + "ns");
	}

	public int getID() {
		return ID;
	}

	public ICounter getMyCounter() {
		return myCounter;
	}
	
}
