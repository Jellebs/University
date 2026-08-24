----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 05/29/2024 11:12:27 AM
-- Design Name: 
-- Module Name: Logik - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;



entity logik is
    Port ( i : in STD_LOGIC_VECTOR (2 downto 0);
           a : out STD_LOGIC_VECTOR (1 downto 0);
           en : in STD_LOGIC);
end logik;

architecture behavioral of logik is 

begin
    a(0) <= i(2) when en = '1' else 'Z';
    a(1) <= '0' when en = '1' else 'Z';
end behavioral;
