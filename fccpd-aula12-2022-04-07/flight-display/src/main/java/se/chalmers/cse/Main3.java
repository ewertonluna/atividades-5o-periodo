package se.chalmers.cse;
import java.util.concurrent.*;

import com.sun.tools.javac.Main;

public class Main3 {

   private static void nap(int millisecs) {
        try {
            Thread.sleep(millisecs);
        } catch (InterruptedException e) {
            System.err.println(e.getMessage());
        }
    }

   private static void addProc(HighLevelDisplay d) {
        for (int i=0; i<180;i++) {
			synchronized (Main3.class) {
				d.addRow("Voo " + i);
				System.out.println("Adicionando");
				nap((int)( 220+(Math.random()*100)));
			}
        }
   }

   private static void deleteProc(HighLevelDisplay d) {
		for (int i=0; i<120;i++) {
			synchronized (Main3.class) {
				d.deleteRow(0);
				System.out.println("Deletando");
				nap((int)( 280+(Math.random()*100)));

			}
		}
    }

    public static void main(String [] args) throws InterruptedException {
		final HighLevelDisplay d = new JDisplay2();

		new Thread() {
			public void run() {
				addProc(d);
			}
		}.start();

		new Thread() {
			public void run() {
				deleteProc(d);
			}
		}.start();

	}
}