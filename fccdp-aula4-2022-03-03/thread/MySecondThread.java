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
		long start = System.nanoTime();
		myCounter.increment();
		long end = System.nanoTime();
		System.out.println("Letra d) Runtime da execução de run() da Thread é de " + (end - start) + "ns");
	}

	public ICounter getMyCounter() {
		return myCounter;
	}

	public int getID() {
		return ID;
	}

}
