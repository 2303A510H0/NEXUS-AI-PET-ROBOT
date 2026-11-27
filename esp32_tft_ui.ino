/*
 NEXUS TFT emotion display starter.
 Requires TFT_eSPI library and correct User_Setup configuration for your TFT.
 Serial commands: happy, neutral, sleep, alert
*/
#include <TFT_eSPI.h>
TFT_eSPI tft = TFT_eSPI();
String command = "neutral";

void drawEyes(uint16_t color, int eyeH, bool closed=false) {
  tft.fillScreen(TFT_BLACK);
  if (closed) {
    tft.drawLine(55, 105, 125, 105, color, 8);
    tft.drawLine(195, 105, 265, 105, color, 8);
  } else {
    tft.fillRoundRect(55, 65, 70, eyeH, 18, color);
    tft.fillRoundRect(195, 65, 70, eyeH, 18, color);
  }
}

void showEmotion(String mood) {
  if (mood == "happy") drawEyes(TFT_CYAN, 65);
  else if (mood == "sleep") drawEyes(TFT_BLUE, 8, true);
  else if (mood == "alert") drawEyes(TFT_RED, 80);
  else drawEyes(TFT_WHITE, 55);
  tft.setTextColor(TFT_WHITE, TFT_BLACK);
  tft.setTextSize(2);
  tft.setCursor(100, 190);
  tft.print("NEXUS");
}

void setup() {
  Serial.begin(115200);
  tft.init();
  tft.setRotation(1);
  showEmotion("neutral");
  Serial.println("NEXUS TFT ready: happy/neutral/sleep/alert");
}

void loop() {
  if (Serial.available()) {
    command = Serial.readStringUntil('\\n');
    command.trim();
    showEmotion(command);
  }
}
