package thread;

import counter.ICounter;

public class MyFourthThread extends Thread {
	private ICounter counter;

	public MyFourthThread(ICounter counter) {
		this.counter = counter;
	}

	@Override
	public void run() {
		while (true) {
			counter.increment();
		}
	}
	
}
