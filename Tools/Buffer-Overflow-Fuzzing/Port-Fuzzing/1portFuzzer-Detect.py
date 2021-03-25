#!/usr/bin/python import socket
import socket, time, sys, argparse

def main():
    parser = argparse.ArgumentParser(description="Port Fuzzer Tool - Chris Buchner")
    parser.add_argument("-i", "--incremental",default=False, action="store_true", help="Incremental Fuzz")
    parser.add_argument("-o", "--onetime",default=False, action="store_true", help="Onetime Fuzz")
    parser.add_argument("-msfs", "--onetimeMSF",default=False, action="store_true", help="MSF String Fuzz")
    parser.add_argument("-t", "--target",default=True, required=True, help="Specify Target")
    parser.add_argument("-p", "--port",default=True, required=True, help="Specify Port")
    parser.add_argument("-bs", "--bufferSize",default=False, required=False, help="Specify Buffer Size")
    parser.add_argument("-br", "--bufferRange",default=False, required=False, help="Specify Buffer Range (ex. \'100,4000\'")
    parser.add_argument("-bi", "--bufferIncrement",default=False, required=False, help="Specify Buffer Increment (ex. 1 or 5)")

    options = parser.parse_args()

    if options.incremental: incremental(options.target,int(options.port),str(options.bufferRange),options.bufferIncrement)
    if options.onetime: onetime(options.target,int(options.port),int(options.bufferSize))
    if options.onetimeMSF: onetimeMSF(options.target,int(options.port))

# 2. Second Step - Identify exact msfOffset with MSF Pattern Create
def onetimeMSF(target,port):
    print "Sending buffer to " + target + ":"+ str(port) + " with MSF Patter Create String"
    
    # Paste MSF Pattern Create String into inputBuffer
    inputBuffer = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy"

    # Customize this buffer for the input you're fuzzing
    # Example: buffer = "\x11(setup sound " + inputBuffer + "\x90\x00#"
    buffer = inputBuffer

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.send(buffer)
    s.close()

# 1. First Step - Identify userOffset Range that works with MSF Pattern Create. 
# 1.a. If MSF Pattern can't identify offset, narrow the increment to identify a more specific offset that will work with MSF Pattern.
def incremental(target,port,bufferRange,bufferIncrement):
    bfrange = bufferRange.split(',')
    print "Buffer Range: " + bfrange[0] + "-" + bfrange[1]
    print "Buffer Increment: " + bufferIncrement + "\n"
    bfsize = int(bfrange[0])

    while(bfsize < int(bfrange[1])):
        try:
            print "Sending buffer to " + target + ":"+ str(port) + " with %s bytes" % str(bfsize)

            inputBuffer = "A" * bfsize
        
            # Customize this buffer for the input you're fuzzing
            # Example: buffer = "\x11(setup sound " + inputBuffer + "\x90\x00#"
            buffer = inputBuffer
        
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(buffer)
            s.close()
        
            bfsize += int(bufferIncrement)
            time.sleep(2)

        except:
            print "\nCould not connect!"
            sys.exit()

def onetime(target,port,buffersize):
    size = buffersize

    try:
        print "Sending buffer to " + target + ":"+ str(port) + " with %s bytes" % size

        inputBuffer = "A" * size

        # buffer = "\x11(setup sound " + inputBuffer + "\x90\x00#"
        # Example: buffer = "\x11(setup sound " + inputBuffer + "\x90\x00#"
        buffer = inputBuffer

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.send(buffer)
        s.close()

    except:
        print "\nCould not connect!"
        sys.exit()

if __name__ == "__main__":
    main()