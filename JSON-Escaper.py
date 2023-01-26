from burp import IBurpExtender, ITab
from java.io import PrintWriter
from java.lang import RuntimeException
from javax.swing import JPanel, JLabel, JTextField, JButton, JScrollPane, JTextArea
import json

class JSONEscaperTab(ITab):
    def __init__(self, extender):
        self._extender = extender
        self._txtPayload = JTextField(20)
        self._btnEscape = JButton("Escape", actionPerformed=self.escape)
        self._txtResult = JTextArea(10,40)
        self._txtResult.setEditable(False)
        
        panel = JPanel()
        panel.add(JLabel("Payload:"))
        panel.add(self._txtPayload)
        panel.add(self._btnEscape)
        scrollPane = JScrollPane(self._txtResult)
        panel.add(scrollPane)
        self.component = panel

    def getTabCaption(self):
        return "JSON Escaper"

    def getUiComponent(self):
        return self.component

    def escape(self, event):
        try:
            payload = self._txtPayload.getText()
            json_escaped = json.dumps(payload, separators=(',', ':'), ensure_ascii=False)
            self._txtResult.setText(json_escaped)
        except Exception as e:
            self._extender._callbacks.printError(str(e))

class BurpExtender(IBurpExtender):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("JSON Escaper")
        callbacks.addSuiteTab(JSONEscaperTab(self))
