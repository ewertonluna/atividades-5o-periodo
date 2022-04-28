package school.cesar.sd.messageconsumer;

import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class MessageProducer implements CommandLineRunner {

    @Autowired
    private RabbitTemplate rabbitTemplate;
    public void run(String... args) throws Exception {
        System.out.println("Sending message...");
        rabbitTemplate.convertAndSend("fanout-exchange", "", "Hello from RabbitMQ!");
    }
}