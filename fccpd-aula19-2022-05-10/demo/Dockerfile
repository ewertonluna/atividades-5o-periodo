FROM maven as builder

ADD . /src/

RUN cd /src && mvn package

FROM openjdk

EXPOSE 8080

COPY --from=builder /src/target/demo-0.0.1-SNAPSHOT.jar /demo.jar

CMD ["java", "-jar", "/demo.jar"]
