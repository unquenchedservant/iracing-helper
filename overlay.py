import wx, json, os.path, irsdk, time
from os import path
import indyTracks
def GetRoundBitmap( w, h, r ):
    maskColor = wx.Colour(0,0,0)
    shownColor = wx.Colour(169,169,169)
    b = wx.Bitmap(w,h)
    dc = wx.MemoryDC(b)
    dc.SetBrush(wx.Brush(maskColor))
    dc.DrawRectangle(0,0,w,h)
    dc.SetBrush(wx.Brush(shownColor))
    dc.SetPen(wx.Pen(shownColor))
    dc.DrawRoundedRectangle(0,0,w,h,r)
    dc.SelectObject(wx.NullBitmap)
    b.SetMaskColour(maskColor)
    return b

def GetRoundShape( w, h, r ):
    return wx.Region( GetRoundBitmap(w,h,r) )

class PracticePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        self.parent = parent

        white = (255,255,255)
        cyan  = (0, 255, 255)

        self.PracticeSizer      = wx.BoxSizer(wx.VERTICAL)
        self.EventSizer     = wx.BoxSizer(wx.HORIZONTAL)
        self.SessionSizer   = wx.BoxSizer(wx.HORIZONTAL)
        self.TopSizer       = wx.BoxSizer(wx.VERTICAL)
        self.PracticeStintSizer = wx.GridBagSizer(3, 2)
        self.IndySizer      = wx.GridBagSizer(4, 2)

        self.EventTypeLabel     = wx.StaticText(self, label="Event Type: ")
        self.EventTypeLabel.SetForegroundColour(cyan)
        font = self.EventTypeLabel.GetFont().Bold()
        self.EventTypeLabel.SetFont(font)
        self.EventType     = wx.StaticText(self, label="None")
        self.EventType.SetForegroundColour(white)
        self.EventSizer.Add(self.EventTypeLabel)
        self.EventSizer.Add(self.EventType)
        self.SessionTypeLabel   = wx.StaticText(self, label="Session Type: ")
        self.SessionTypeLabel.SetForegroundColour(cyan)
        self.SessionTypeLabel.SetFont(font)
        self.SessionType   = wx.StaticText(self, label="None")
        self.SessionType.SetForegroundColour(white)
        self.SessionSizer.Add(self.SessionTypeLabel)
        self.SessionSizer.Add(self.SessionType)
        self.TopSizer.Add(self.EventSizer)
        self.TopSizer.Add(self.SessionSizer)
        self.LapSincePitLabel   = wx.StaticText(self, label="Laps Since Pit: ")
        self.LapSincePitLabel.SetForegroundColour(cyan)
        self.LapSincePitLabel.SetFont(font)
        self.LongestRunLabel    = wx.StaticText(self, label="Longest Run: ")
        self.LongestRunLabel.SetForegroundColour(cyan)
        self.LongestRunLabel.SetFont(font)
        self.PlayerLapLabel     = wx.StaticText(self, label="Your Lap: ")
        self.PlayerLapLabel.SetForegroundColour(cyan)
        self.PlayerLapLabel.SetFont(font)
        self.LapSincePit   = wx.StaticText(self, label="0")
        self.LapSincePit.SetForegroundColour(white)
        self.LongestRun    = wx.StaticText(self, label="0")
        self.LongestRun.SetForegroundColour(white)
        self.PlayerLap     = wx.StaticText(self, label="0")
        self.PlayerLap.SetForegroundColour(white)
        self.PracticeStintSizer.Add(self.LapSincePitLabel, (1, 0))
        self.PracticeStintSizer.Add(self.LapSincePit, (1, 1))
        self.PracticeStintSizer.Add(self.LongestRunLabel, (2, 0))
        self.PracticeStintSizer.Add(self.LongestRun, (2, 1))
        self.PracticeStintSizer.Add(self.PlayerLapLabel, (3, 0))
        self.PracticeStintSizer.Add(self.PlayerLap, (3, 1))
        self.WeightJackerLabel  = wx.StaticText(self, label="Weight Jacker: ")
        self.WeightJackerLabel.SetForegroundColour(cyan)
        self.WeightJackerLabel.SetFont(font)
        self.FrontARBLabel = wx.StaticText(self, label="Front ARB: ")
        self.FrontARBLabel.SetForegroundColour(cyan)
        self.FrontARBLabel.SetFont(font)
        self.RearARBLabel = wx.StaticText(self, label="Rear ARB: ")
        self.RearARBLabel.SetForegroundColour(cyan)
        self.RearARBLabel.SetFont(font)
        self.IndyWeight  = wx.StaticText(self, label="0")
        self.IndyWeight.SetForegroundColour(white)
        self.IndyFront   = wx.StaticText(self, label="0")
        self.IndyFront.SetForegroundColour(white)
        self.IndyRear    = wx.StaticText(self, label="0")
        self.IndyRear.SetForegroundColour(white)
        self.IndySizer.Add(self.WeightJackerLabel, (1, 0))
        self.IndySizer.Add(self.IndyWeight, (1, 1))
        self.IndySizer.Add(self.FrontARBLabel, (2, 0))
        self.IndySizer.Add(self.IndyFront, (2, 1))
        self.IndySizer.Add(self.RearARBLabel, (3, 0))
        self.IndySizer.Add(self.IndyRear, (3, 1))

        self.PracticeSizer.Add(self.TopSizer)
        self.PracticeSizer.Add(self.PracticeStintSizer)
        self.PracticeSizer.Add(self.IndySizer)

        self.SetSizerAndFit(self.PracticeSizer)

    def hideIndy(self):
        self.PracticeSizer.Hide(self.IndySizer)
        self.Update()
    def showIndy(self):
        self.PracticeSizer.Show(self.IndySizer)
        self.Layout()
    def UpdateSession(self, sessionType):
        self.SessionType.SetLabel("{}".format(sessionType))
        self.Fit()
    def UpdateEvent(self, eventType):
        self.EventType.SetLabel("{}".format(eventType))
        self.Fit()
class RacePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        self.parent = parent

        white = (255,255,255)
        cyan  = (0, 255, 255)

        self.RaceSizer      = wx.BoxSizer(wx.VERTICAL)
        self.EventSizer     = wx.BoxSizer(wx.HORIZONTAL)
        self.SessionSizer   = wx.BoxSizer(wx.HORIZONTAL)
        self.TopSizer       = wx.BoxSizer(wx.VERTICAL)
        self.RaceStintSizer = wx.GridBagSizer(5, 6)
        self.IndySizer      = wx.GridBagSizer(4, 2)
        self.RaceLapsSizer  = wx.GridBagSizer(3, 2)
        self.StatSizer      = wx.GridBagSizer(4, 2)

        self.EventTypeLabel     = wx.StaticText(self, label="Event Type: ")
        self.EventTypeLabel.SetForegroundColour(cyan)
        font = self.EventTypeLabel.GetFont().Bold()
        self.EventTypeLabel.SetFont(font)
        self.EventType     = wx.StaticText(self, label="None")
        self.EventType.SetForegroundColour(white)
        self.EventSizer.Add(self.EventTypeLabel)
        self.EventSizer.Add(self.EventType)
        self.SessionTypeLabel   = wx.StaticText(self, label="Session Type: ")
        self.SessionTypeLabel.SetForegroundColour(cyan)
        self.SessionTypeLabel.SetFont(font)
        self.SessionType   = wx.StaticText(self, label="None")
        self.SessionType.SetForegroundColour(white)
        self.SessionSizer.Add(self.SessionTypeLabel)
        self.SessionSizer.Add(self.SessionType)
        self.TopSizer.Add(self.EventSizer)
        self.TopSizer.Add(self.SessionSizer)
        self.LapSincePitLabel   = wx.StaticText(self, label="Laps Since Pit: ")
        self.LapSincePitLabel.SetForegroundColour(cyan)
        self.LapSincePitLabel.SetFont(font)
        self.AmountGreenLabel   = wx.StaticText(self, label="Green: ")
        self.AmountGreenLabel.SetForegroundColour(cyan)
        self.AmountGreenLabel.SetFont(font)
        self.AmountPacingLabel  = wx.StaticText(self, label="Pacing: ")
        self.AmountPacingLabel.SetForegroundColour(cyan)
        self.AmountPacingLabel.SetFont(font)
        self.LongestRunLabel    = wx.StaticText(self, label="Longest Run: ")
        self.LongestRunLabel.SetForegroundColour(cyan)
        self.LongestRunLabel.SetFont(font)
        self.LapSincePit   = wx.StaticText(self, label="0")
        self.LapSincePit.SetForegroundColour(white)
        self.AmountGreen   = wx.StaticText(self, label="0")
        self.AmountGreen.SetForegroundColour(white)
        self.AmountPacing  = wx.StaticText(self, label="0")
        self.AmountPacing.SetForegroundColour(white)
        self.LongestRun    = wx.StaticText(self, label="0")
        self.LongestRun.SetForegroundColour(white)
        self.RaceStintSizer.Add(self.LapSincePitLabel, (1, 0))
        self.RaceStintSizer.Add(self.LapSincePit, (1, 1))
        self.RaceStintSizer.Add(self.AmountGreenLabel, (2, 0))
        self.RaceStintSizer.Add(self.AmountGreen, (2, 1))
        self.RaceStintSizer.Add(self.AmountPacingLabel, (3, 0))
        self.RaceStintSizer.Add(self.AmountPacing, (3, 1))
        self.RaceStintSizer.Add(self.LongestRunLabel, (4, 0))
        self.RaceStintSizer.Add(self.LongestRun, (4, 1))
        self.LeaderOnLapLabel = wx.StaticText(self, label="Lead Lap: ")
        self.LeaderOnLapLabel.SetForegroundColour(cyan)
        self.LeaderOnLapLabel.SetFont(font)
        self.PlayerLapLabel = wx.StaticText(self, label="Your Lap: ")
        self.PlayerLapLabel.SetForegroundColour(cyan)
        self.PlayerLapLabel.SetFont(font)
        self.LeadLap = wx.StaticText(self, label="0")
        self.LeadLap.SetForegroundColour(white)
        self.PlayerLap = wx.StaticText(self, label="0")
        self.PlayerLap.SetForegroundColour(white)
        self.RaceLapsSizer.Add(self.LeaderOnLapLabel, (1, 0))
        self.RaceLapsSizer.Add(self.LeadLap, (1, 1))
        self.RaceLapsSizer.Add(self.PlayerLapLabel, (2, 0))
        self.RaceLapsSizer.Add(self.PlayerLap, (2, 1))
        self.WeightJackerLabel  = wx.StaticText(self, label="Weight Jacker: ")
        self.WeightJackerLabel.SetForegroundColour(cyan)
        self.WeightJackerLabel.SetFont(font)
        self.FrontARBLabel = wx.StaticText(self, label="Front ARB: ")
        self.FrontARBLabel.SetForegroundColour(cyan)
        self.FrontARBLabel.SetFont(font)
        self.RearARBLabel = wx.StaticText(self, label="Rear ARB: ")
        self.RearARBLabel.SetForegroundColour(cyan)
        self.RearARBLabel.SetFont(font)
        self.IndyWeight  = wx.StaticText(self, label="0")
        self.IndyWeight.SetForegroundColour(white)
        self.IndyFront   = wx.StaticText(self, label="0")
        self.IndyFront.SetForegroundColour(white)
        self.IndyRear    = wx.StaticText(self, label="0")
        self.IndyRear.SetForegroundColour(white)
        self.IndySizer.Add(self.WeightJackerLabel, (1, 0))
        self.IndySizer.Add(self.IndyWeight, (1, 1))
        self.IndySizer.Add(self.FrontARBLabel, (2, 0))
        self.IndySizer.Add(self.IndyFront, (2, 1))
        self.IndySizer.Add(self.RearARBLabel, (3, 0))
        self.IndySizer.Add(self.IndyRear, (3, 1))
        self.TotalGreenLabel    = wx.StaticText(self, label="Total Green: ")
        self.TotalGreenLabel.SetForegroundColour(cyan)
        self.TotalGreenLabel.SetFont(font)
        self.LongestGreenLabel  = wx.StaticText(self, label="Longest Green: ")
        self.LongestGreenLabel.SetForegroundColour(cyan)
        self.LongestGreenLabel.SetFont(font)
        self.TotalYellowLabel   = wx.StaticText(self, label="Total Yellow: ")
        self.TotalYellowLabel.SetForegroundColour(cyan)
        self.TotalYellowLabel.SetFont(font)
        self.TotalCautionsLabel = wx.StaticText(self, label= "Total Cautions: ")
        self.TotalCautionsLabel.SetForegroundColour(cyan)
        self.TotalCautionsLabel.SetFont(font)
        self.LongestGreen  = wx.StaticText(self, label="0")
        self.LongestGreen.SetForegroundColour(white)
        self.TotalGreen    = wx.StaticText(self, label="0")
        self.TotalGreen.SetForegroundColour(white)
        self.TotalYellow   = wx.StaticText(self, label="0")
        self.TotalYellow.SetForegroundColour(white)
        self.TotalCautions = wx.StaticText(self, label="0")
        self.TotalCautions.SetForegroundColour(white)
        self.StatSizer.Add(self.TotalGreenLabel, (1, 0))
        self.StatSizer.Add(self.TotalGreen, (1, 1))
        self.StatSizer.Add(self.LongestGreenLabel, (2, 0))
        self.StatSizer.Add(self.LongestGreen, (2, 1))
        self.StatSizer.Add(self.TotalYellowLabel, (3, 0))
        self.StatSizer.Add(self.TotalYellow, (3, 1))
        self.StatSizer.Add(self.TotalCautionsLabel, (4, 0))
        self.StatSizer.Add(self.TotalCautions, (4, 1))

        self.RaceSizer.Add(self.TopSizer)
        self.RaceSizer.Add(self.RaceStintSizer)
        self.RaceSizer.Add(self.IndySizer)
        self.RaceSizer.Add(self.RaceLapsSizer)
        self.RaceSizer.Add(self.StatSizer)

        self.SetSizerAndFit(self.RaceSizer)

    def hideIndy(self):
        self.RaceSizer.Hide(self.IndySizer)
        self.Layout()
    def showIndy(self):
        self.RaceSizer.Show(self.IndySizer)
        self.Layout()

    def UpdateSession(self, sessionType):
        self.SessionType.SetLabel("{}".format(sessionType))
        self.Fit()
    def UpdateEvent(self, eventType):
        self.EventType.SetLabel("{}".format(eventType))
        self.Fit()

class FancyFrame(wx.Frame):
    def __init__(self):
        style = ( wx.CLIP_CHILDREN | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR |
                  wx.NO_BORDER | wx.FRAME_SHAPED  )
        wx.Frame.__init__(self, None, title='Fancy', style = style)
        if path.exists("position.json"):
            with open("position.json") as json_file:
                pos = json.load(json_file)
                self.SetPosition((pos['x'], pos['y']))
        else:
            self.SetPosition((400, 300))

        self.SetSize( (200, 400) )
        self.SetTransparent( 200 )
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
        self.practice_panel = PracticePanel(self)
        self.race_panel = RacePanel(self)
        self.race_panel.Hide()

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.mainSizer.Add(self.practice_panel, 1, wx.EXPAND)
        self.mainSizer.Add(self.race_panel, 1, wx.EXPAND)
        self.SetSizer(self.mainSizer)

        #iracing data
        self.ir = irsdk.IRSDK()
        self.panel = None
        self.weight_change  = False
        self.front_change   = False
        self.rear_change    = False
        self.wblink_total   = 0
        self.fblink_total   = 0
        self.rblink_total   = 0
        self.wchange_count  = 0
        self.fchange_count  = 0
        self.rchange_count  = 0
        self.color_timer    = 10
        self.blink_max      = 6
        self.weight_color   = "white"
        self.front_color    = "white"
        self.rear_color     = "white"
        self.first_run      = True
        self.ir_connected   = False
        self.wInfo          = None
        self.event_type     = None
        self.event_location = None
        self.session_num    = 0
        self.session_type   = None
        self.is_indy        = False
        self.in_pit         = False
        self.pacing         = False
        self.show           = False
        self.is_race        = False
        self.practice_prepped = False
        self.race_prepped     = False
        self.current_stint  = 0
        self.green_laps     = 0
        self.pace_laps      = 0
        self.longest_stint  = 0
        self.lead_lap       = 0
        self.laps_driven    = 0
        self.total_yellow   = 0
        self.current_green  = 0
        self.total_green    = 0
        self.longest_green  = 0
        self.total_cautions = 0
        self.indy_weight    = 0
        self.indy_front     = 0
        self.indy_rear      = 0


        self.Bind(wx.EVT_KEY_UP, self.OnKeyDown)
        self.Bind(wx.EVT_MOTION, self.OnMouse)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.check_iRacing)
        self.timer.Start(60)
        black = (0,0,0)
        white = (255,255,255)
        cyan  = (0, 255, 255)


        self.SetBackgroundColour(black)
        if wx.Platform == '__WXGTK__':
            self.Bind(wx.EVT_WINDOW_CREATE, self.SetRoundShape)
        else:
            self.SetRoundShape()
        self.Show(False)

    def ResetInfo(self):
        self.ir_connected   = False
        self.weight_change  = False
        self.front_change   = False
        self.rear_change    = False
        self.wblink_total   = 0
        self.fblink_total   = 0
        self.rblink_total   = 0
        self.wchange_count  = 0
        self.fchange_count  = 0
        self.rchange_count  = 0
        self.weight_color   = "white"
        self.front_color    = "white"
        self.rear_color     = "white"
        self.wInfo          = None
        self.event_type     = None
        self.event_location = None
        self.session_num    = 0
        self.session_type   = None
        self.is_indy        = False
        self.in_pit         = False
        self.pacing         = False
        self.show           = False
        self.is_race        = False
        self.practice_prepped = False
        self.race_prepped     = False
        self.current_stint  = 0
        self.green_laps     = 0
        self.pace_laps      = 0
        self.longest_stint  = 0
        self.lead_lap       = 0
        self.laps_driven    = 0
        self.total_yellow   = 0
        self.current_green  = 0
        self.longest_green  = 0
        self.total_green    = 0
        self.total_cautions = 0
        self.indy_weight    = 0
        self.indy_front     = 0
        self.indy_rear      = 0
        self.updateIndy()
        self.updateSessionRow()
        if self.panel == self.race_panel:
            self.updateStintLaps()
            self.updateRaceLaps()
            self.updateCautions()
        else:
            self.updatePracticeStintLaps()

    def GetWeekendInfo(self):
        wInfo = self.ir['WeekendInfo']
        if wInfo:
            self.wInfo = wInfo
            eType = self.wInfo['EventType']
            if eType != self.event_type:
                self.event_type = eType
            eLocation = self.wInfo['TrackName']
            if eLocation != self.event_location:
                self.event_location = eLocation

    def GetSessionNumber(self):
        sessionNum = self.ir['SessionNum']
        if sessionNum:
            if sessionNum != self.session_num:
                self.session_num = sessionNum

    def GetSession(self):
        session = self.ir['SessionInfo']
        if session:
            session = session['Sessions'][self.session_num]
            sessionType = session['SessionType']
            if sessionType:
                if sessionType != self.session_type:
                    self.session_type = sessionType


    def CheckIndy(self):
        driverInfo = self.ir['DriverInfo']
        if driverInfo:
            drivers = driverInfo['Drivers']
            for driver in drivers:
                if driver['CarIdx'] == driverInfo['DriverCarIdx']:
                    car_name = driver['CarScreenNameShort']
                    if car_name == "IR18":
                        self.is_indy = True
                    else:
                        self.is_indy = False

    def CheckPit(self):
        inPit = self.ir['PlayerCarInPitStall']
        if inPit != self.in_pit:
            self.in_pit = inPit


    def GetLeadLap(self):
        raceLaps = self.ir['RaceLaps']
        if raceLaps and raceLaps != self.lead_lap:
            self.lead_lap = raceLaps
            if raceLaps > 1 and self.pacing == True:
                self.total_yellow += 1
                self.current_green = 0
            elif raceLaps > 1 and self.pacing == False:
                self.total_green += 1
                self.current_green += 1
                if self.current_green > self.longest_green:
                    self.longest_green = self.current_green
            self.updateRaceLaps()

    def GetLaps(self):
        lap = self.ir['Lap']
        if lap:
            if lap != self.laps_driven:
                self.laps_driven = lap
                if self.laps_driven > 0:
                    self.current_stint += 1
                    if self.current_stint > self.longest_stint:
                        self.longest_stint = self.current_stint
                    if self.is_race:
                        if self.pacing:
                            self.pace_laps += 1
                        else:
                            self.green_laps += 1
                self.updateStintLaps()
    def GetPracticeLaps(self):
        lap = self.ir['Lap']
        if lap:
            if lap != self.laps_driven:
                self.laps_driven = lap
                if self.laps_driven > 0:
                    self.current_stint += 1
                    if self.current_stint > self.longest_stint:
                        self.longest_stint = self.current_stint
                self.updatePracticeStintLaps()
    def GetIndy(self):
        lap_weight = 0
        lap_front_arb = 0
        lap_rear_arb = 0
        if self.is_indy and self.event_location:
            if not os.path.exists("indycar/{}.json".format(self.event_location)):
                self.timer.Stop()
                if not os.path.exists("indycar/"):
                    os.mkdir("indycar")
                while True:
                    indyTracks.start(self.event_location)
                    break
                self.timer.Start(60)

            with open("indycar/{}.json".format(self.event_location), "r") as f:
                data = json.load(f)
                for p in data['lap']:
                    if self.session_type == "race":
                        if p['lap'] == self.green_laps and self.green_laps <= 32:
                            lap_weight = p['weight']
                            lap_front_arb = p['front']
                            lap_rear_arb  = p['rear']
                    else:
                        if p['lap'] == self.current_stint and self.current_stint <= 32:
                            lap_weight = p['weight']
                            lap_front_arb = p['front']
                            lap_rear_arb = p['rear']

                if lap_weight >= 0 and (self.indy_weight != lap_weight):
                    self.weight_change = True
                    self.weight_color = "white"
                    self.indy_weight = lap_weight
                if lap_front_arb >= 0 and (self.indy_front != lap_front_arb):
                    self.front_change = True
                    self.front_color = "white"
                    self.indy_front = lap_front_arb
                if lap_rear_arb >= 0 and (self.indy_rear != lap_rear_arb):
                    self.rear_change = True
                    self.rear_color = "white"
                    self.indy_rear = lap_rear_arb
            self.updateIndy()

    def GetFlag(self):
        flags = {
            "Checkered" : 0x0001,
            "White"            : 0x0002,
            "Green"            : 0x0004,
            "Yellow"           : 0x0008,
            "Red"              : 0x0010,
            "Blue"             : 0x0020,
            "Debris"           : 0x0040,
            "Crossed"          : 0x0080,
            "yellow_waving"    : 0x0100,
            'one_lap_to_green' : 0x0200,
            'green_held'       : 0x0400,
            'ten_to_go'       : 0x0800,
            'five_to_go'       : 0x1000,
            'random_waving'    : 0x2000,
            'caution'          : 0x4000,
            'caution_waving'   : 0x8000,

        # drivers black flags
            'black'      : 0x010000,
            'disqualify' : 0x020000,
            'servicible' : 0x040000, # car is allowed service (not a flag)
            'furled'     : 0x080000,
            'repair'     : 0x100000,

        # start lights
            'start_hidden' : 0x10000000,
            'start_ready'  : 0x20000000,
            'start_set'    : 0x40000000,
            'start_go'     : 0x80000000
        }
        flag = self.ir['SessionFlags']
        if flag:
            for f, number in flags.items():
                if number & flag:
                    if f == "Green":
                        if self.pacing:
                            self.pacing = False
                    elif f == "caution" or f == "caution_waving":
                        if not self.pacing:
                            self.pacing = True
                            self.total_cautions += 1
                            self.updateCautions()
                    elif f == "one_lap_to_green":
                        if not self.pacing:
                            self.pacing = True
    def check_iRacing(self, event):
        if self.ir_connected and not (self.ir.is_initialized and self.ir.is_connected):
            self.ir_connected = False
            self.ir.shutdown()
            self.ResetInfo()
            self.Show(False)
        elif not self.ir_connected and self.ir.startup() and self.ir.is_initialized and self.ir.is_connected:
            self.ir_connected = True
        if self.ir_connected:
            self.iRacing()
        if not self.ir_connected:
            self.Show(False)

    def iRacing(self):
        self.ir.freeze_var_buffer_latest()
        self.GetWeekendInfo()
        self.GetSessionNumber()
        self.GetSession()
        self.CheckIndy()
        self.CheckPit()
        if self.session_num == 2:
            self.is_race = True
            if self.panel:
                if self.panel == self.practice_panel:
                    self.panel = self.race_panel
                    self.ResetInfo()
                self.practice_panel.Hide()
                self.race_panel.Show()
            if not self.panel:
                self.practice_panel.Hide()
                self.race_panel.Show()
                self.panel = self.race_panel
            self.race_panel.UpdateSession(self.session_type)
            self.race_panel.UpdateEvent(self.event_type)
            if not self.is_indy:
                self.race_panel.hideIndy()
            if self.is_indy:
                self.race_panel.showIndy()
            self.GetRaceInfo()
            self.Show(True)
        else:
            if self.panel:
                if self.panel == self.race_panel:
                    self.ResetInfo()
                self.practice_panel.Show()
                self.race_panel.Hide()
                self.panel = self.practice_panel
            if not self.panel:
                self.practice_panel.Show()
                self.race_panel.Hide()
                self.panel = self.practice_panel
            self.practice_panel.UpdateEvent(self.event_type)
            self.practice_panel.UpdateSession(self.session_type)
            if not self.is_indy:
                self.practice_panel.hideIndy()
            if self.is_indy:
                self.practice_panel.showIndy()
            self.GetPracticeInfo()
            self.Show(True)



    def GetPracticeInfo(self):
        self.GetPracticeLaps()
        if self.is_indy:
            self.GetIndy()
        if self.in_pit:
            self.current_stint = 0
            if self.laps_driven == 1:
                self.longest_stint = 0
            self.updatePracticeStintLaps()

    def GetRaceInfo(self):
        self.GetFlag()
        self.GetLaps()
        self.GetLeadLap()
        if self.is_indy:
            self.GetIndy()
        if self.in_pit:
            self.current_stint = 0
            self.green_laps = 0
            self.pace_laps = 0
            if self.laps_driven == 1:
                self.longest_stint = 0
            self.updateStintLaps()

    def updateEventRow(self):
        self.panel.EventType.SetLabel("{}".format(self.event_type))
    def updateSessionRow(self):
        self.panel.SessionType.SetLabel("{}".format(self.session_type))
    def updateStintLaps(self):
        self.panel.LapSincePit.SetLabel("{}".format(self.current_stint))
        self.panel.AmountGreen.SetLabel("{}".format(self.green_laps))
        self.panel.AmountPacing.SetLabel("{}".format(self.pace_laps))
        self.panel.LongestRun.SetLabel("{}".format(self.longest_stint))
        self.panel.PlayerLap.SetLabel("{}".format(self.laps_driven))
        self.panel.Layout()
    def updatePracticeStintLaps(self):
        self.panel.LapSincePit.SetLabel("{}".format(self.current_stint))
        self.panel.LongestRun.SetLabel("{}".format(self.longest_stint))
        self.panel.PlayerLap.SetLabel("{}".format(self.laps_driven))
        self.panel.Layout()
    def updateRaceLaps(self):
        self.panel.LeadLap.SetLabel("{}".format(self.lead_lap))
        self.panel.TotalYellow.SetLabel("{}".format(self.total_yellow))
        self.panel.TotalGreen.SetLabel("{}".format(self.total_green))
        self.panel.LongestGreen.SetLabel("{}".format(self.longest_green))
        self.panel.TotalCautions.SetLabel("{}".format(self.total_cautions))
        self.panel.Layout()
    def updateIndy(self):
        if self.weight_change:
            self.wchange_count += 1
            if self.wchange_count == self.color_timer:
                self.wchange_count = 0
                self.wblink_total += 1
                if self.weight_color == "red":
                    self.panel.IndyWeight.SetForegroundColour(self.white)
                    self.panel.IndyWeight.Refresh()
                    self.panel.IndyWeight.Update()
                    self.weight_color = "white"
                elif self.weight_color == "white":
                    self.panel.IndyWeight.SetForegroundColour(self.red)
                    self.panel.IndyWeight.Refresh()
                    self.panel.IndyWeight.Update()
                    self.weight_color = "red"
            if self.wblink_total == self.blink_max:
                self.weight_change = False
                self.wblink_total = 0
                self.wchange_count = 0
                self.weight_color = "white"
                self.panel.IndyWeight.SetForegroundColour(self.white)
        self.panel.IndyWeight.SetLabel("{}".format(self.indy_weight))
        self.panel.IndyFront.SetLabel("{}".format(self.indy_front))
        if self.front_change:
            self.fchange_count += 1
            if self.fchange_count == self.color_timer:
                self.fchange_count = 0
                self.fblink_total += 1
                if self.front_color == "red":
                    self.front_color = "white"
                    self.panel.IndyFront.SetForegroundColour(self.white)
                    self.panel.IndyFront.Refresh()
                    self.panel.IndyFront.Update()
                elif self.front_color == "white":
                    self.front_color = "red"
                    self.panel.IndyFront.SetForegroundColour(self.red)
                    self.panel.IndyFront.Refresh()
                    self.panel.IndyFront.Update()
            if self.fblink_total == self.blink_max:
                self.front_change = False
                self.fblink_total = 0
                self.fchange_count = 0
                self.front_color = "white"
                self.panel.IndyFront.SetForegroundColour(self.white)
        self.panel.IndyRear.SetLabel("{}".format(self.indy_rear))
        if self.rear_change:
            self.rchange_count += 1
            if self.rchange_count == self.color_timer:
                self.rchange_count = 0
                self.rblink_total += 1
                if self.rear_color == "red":
                    self.panel.IndyRear.SetForegroundColour(wx.Colour(self.white))
                    self.panel.IndyRear.Refresh()
                    self.panel.IndyRear.Update()
                    self.rear_color = "white"
                elif self.rear_color == "white":
                    self.panel.IndyRear.SetForegroundColour(wx.Colour(self.red))
                    self.panel.IndyRear.Refresh()
                    self.panel.IndyRear.Update()
                    self.rear_color = "red"
            if self.rblink_total == self.blink_max:
                self.rear_change = False
                self.rblink_total = 0
                self.rchange_count = 0
                self.rear_color = "white"
                self.panel.IndyRear.SetForegroundColour(self.white)
    def updateCautions(self):
        self.panel.TotalCautions.SetLabel("{}".format(self.total_cautions))
        self.panel.Layout()


    def SetRoundShape(self, event=None):
        w, h = self.GetSize()
        self.SetShape(GetRoundShape( w,h, 10 ) )

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc = wx.GCDC(dc)
        w, h = self.GetSize()
        r = 10
        dc.SetPen( wx.Pen("#000000", width = 2 ) )
        dc.SetBrush( wx.Brush("#000000") )
        dc.DrawRoundedRectangle( 0,0,w,h,r )

    def OnKeyDown(self, event):
        """quit if user press q or Esc"""
        if event.GetKeyCode() == 27 or event.GetKeyCode() == ord('Q'): #27 is Esc
            self.Close(force=True)
        elif event.GetKeyCode() == ord('E'):
            while True:
                indyTracks.start(self.event_location)
                break
            self.timer.Start(60)

    def OnMouse(self, event):
        """implement dragging"""
        if not event.Dragging():
            self._dragPos = None
            return
        if not self._dragPos:
            self._dragPos = event.GetPosition()
        else:
            pos = event.GetPosition()
            displacement = self._dragPos - pos
            self.SetPosition( self.GetPosition() - displacement )
            point = {}
            point['x'] = self.GetPosition().x
            point['y'] = self.GetPosition().y
            with open("position.json", "w+") as f:
                f.write(json.dumps(point))
