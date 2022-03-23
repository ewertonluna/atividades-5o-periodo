package counter;

// Solução da letra A'
public class SequentialCounter implements ICounter {
	int value = 0;
	
	@Override
	public void increment() {
		value += 1;
	}

	@Override
	public int getValue() {
		return value;
	}
}
