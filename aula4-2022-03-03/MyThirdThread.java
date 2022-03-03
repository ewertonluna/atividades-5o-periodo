public class MyThirdThread extends Thread {
	private MyCounter myCounter;
	private int id;

	public MyThirdThread(int id, MyCounter myCounter) {
		this.id = id;
		this.myCounter = myCounter;
	}

	@Override
	public void run() {
		myCounter.increment();
		System.out.println("ID da thread: " + id);
	}
	
}
