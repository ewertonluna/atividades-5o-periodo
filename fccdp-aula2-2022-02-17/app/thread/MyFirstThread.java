package app.thread;

/**
 * Essa classe é usada para letra a
 */
public class MyFirstThread extends Thread {
	private int id;

	public MyFirstThread(int id) {
		this.id = id;
	}

	public void run() {
		System.out.println("Hello Thread! ID da thread: " + id);
	}
}
