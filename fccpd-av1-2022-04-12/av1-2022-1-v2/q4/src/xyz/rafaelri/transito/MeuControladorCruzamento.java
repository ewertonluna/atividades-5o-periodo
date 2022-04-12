package xyz.rafaelri.transito;

public class MeuControladorCruzamento implements ControladorCruzamento{

	@Override
    public synchronized void entrarHorizontal() {
        try {
            wait();
			sairHorizontal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @Override
    public synchronized void sairHorizontal() {
    }

    @Override
    public synchronized void entrarVertical() {
		sairVertical();
    }

    @Override
    public synchronized void sairVertical() {
		notifyAll();
    }
	
}