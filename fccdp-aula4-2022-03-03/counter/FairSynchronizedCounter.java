package counter;

import java.util.Comparator;
import java.util.LinkedList;
import java.util.ListIterator;
public class FairSynchronizedCounter implements ICounter {
	private int value = 0;
	private LinkedList<Thread> threads;
	private Thread allowedThread;
	private ListIterator<Thread> threadsIterator; 

	@Override
	public synchronized void increment() {
		if (threads == null) {
			throw new IllegalStateException("You must set the list of threads first before incrementing.");
		} 
		if (allowedThread.getId() != Thread.currentThread().getId()) {
			try {
				wait();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		System.out.println("Incrementing counter value from Thread ID: " + allowedThread.getId());
		value++;
		allowedThread = getNextAllowedThread();
		notifyAll();
	}

	@Override
	public int getValue() {
		return value;
	}

	public void setThreads(LinkedList<Thread> threads) {
		if (this.threads != null) {
			throw new IllegalStateException("\'threads\' is already set. You cannot set it again");
		}
		if (threads.size() == 0) {
			throw new IllegalStateException("'\threads\' list must have at least one thread in it");
		}
		this.threads = sortThreads(threads);
		threadsIterator = threads.listIterator();
		allowedThread = getNextAllowedThread();
	}

	private LinkedList<Thread> sortThreads(LinkedList<Thread> threads) {
		threads.sort(new Comparator<Thread>() {
			@Override
			public int compare(Thread thread1, Thread thread2) {
				return (int) (thread1.getId() - thread2.getId());
			}
		});
		return threads;
	}

	private Thread getNextAllowedThread() {
		if (!threadsIterator.hasNext()) {
			threadsIterator = threads.listIterator();
		}
		return threadsIterator.next();
	}
	
}
