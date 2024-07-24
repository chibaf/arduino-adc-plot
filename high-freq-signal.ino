void setup() {
Serial.begin(2000000);
}
int cycle=20000;
int i;
float pi=3.1415;
float wave;

void loop() {
  i=i+1;
  i=i % cycle;
  wave=sin(2.0*pi*float(i)/float(cycle));
  Serial.println(wave);  // put your main code here, to run repeatedly:
}
