library IEEE;
use IEEE.Std_logic_1164.all;
use IEEE.Numeric_Std.all;

entity logik_tb is
end;

architecture bench of logik_tb is

  component logik
      Port ( i : in STD_LOGIC_VECTOR (2 downto 0);
             a : out STD_LOGIC_VECTOR (1 downto 0);
             en : in STD_LOGIC);
  end component;

  signal i: STD_LOGIC_VECTOR (2 downto 0);
  signal a: STD_LOGIC_VECTOR (1 downto 0);
  signal en: STD_LOGIC;

begin

  uut: logik port map ( i  => i,
                        a  => a,
                        en => en );

  stimulus: process
  begin
  
    -- Put initialisation code here
--                                      Enable == 0 
    en <= '0';
    i <= ('0', '0', '0'); 
    wait 10ns
    
    en <= '0';
    i <= ('0', '0', '1'); 
    wait 10ns
    
    en <= '0';
    i <= ('0', '1', '0'); 
    wait 10ns
    
    en <= '0';
    i <= ('0', '1', '1'); 
    wait 10ns
    
    en <= '0';
    i <= ('1', '0', '0'); 
    wait 10ns
    
    en <= '0';
    i <= ('1', '0', '1'); 
    wait 10ns
    
    en <= '0';
    i <= ('1', '1', '0'); 
    wait 10ns
    
    en <= '0';
    i <= ('1', '1', '1'); 
    wait 10ns
    
    --                                      Enable == 1   
    
    en <= '1';
    i <= ('0', '0', '0'); 
    wait 10ns
    
    en <= '1';
    i <= ('0', '0', '1'); 
    wait 10ns
    
    en <= '1';
    i <= ('0', '1', '0'); 
    wait 10ns
    
    en <= '1';
    i <= ('0', '1', '1'); 
    wait 10ns
    
    en <= '1';
    i <= ('1', '0', '0'); 
    wait 10ns
    
    en <= '1';
    i <= ('1', '0', '1'); 
    wait 10ns
    
    en <= '1';
    i <= ('1', '1', '0'); 
    wait 10ns
    
    en <= '1';
    i <= ('1', '1', '1'); 


    -- Put test bench stimulus code here

    wait;
  end process;


end;
  