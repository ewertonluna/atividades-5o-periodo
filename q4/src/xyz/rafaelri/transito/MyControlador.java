package xyz.rafaelri.transito;

public class MyControlador implements ControladorCruzamento {
    private boolean isCrossing;

    @Override
    public synchronized void entrarHorizontal() {
        if (isCrossing){
            try {
                this.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        } else {
            isCrossing = true;
        }    
    }

    @Override
    public synchronized void sairHorizontal() {
        isCrossing = false;
        notify();
    }

    @Override
    public synchronized void entrarVertical() {
        if (isCrossing){
            try {
                this.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        } else {
            isCrossing = true;
        }  
    }

    @Override
    public synchronized void sairVertical() {
        isCrossing = false;
        notify();
    }
    
}
